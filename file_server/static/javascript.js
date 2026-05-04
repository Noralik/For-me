let currentFile = null;

// ===================== INIT =====================
document.addEventListener("DOMContentLoaded", () => {
    loadGallery();
    loadMyGallery();

    document.getElementById("uploadForm").addEventListener("submit", uploadFile);
});

// ===================== LOAD =====================
async function loadGallery() {
    const res = await fetch("/files");
    const data = await res.json();
    renderGallery(data, "gallery");
}

async function loadMyGallery() {
    const res = await fetch("/my_files");
    const data = await res.json();
    renderGallery(data, "my_gallery");
}

// ===================== RENDER =====================
function renderGallery(files, targetId) {
    const box = document.getElementById(targetId);
    box.innerHTML = "";

    files.forEach(file => {
        const div = document.createElement("div");
        div.className = "photo";

        div.innerHTML = `
            <img src="${file.url}" onclick="openView(${file.id})">

            <div class="info">
                <b>${file.title || ""}</b><br>
                ${file.description || ""}<br>

                <small>
                    📅 ${file.created_at || ""}<br>
                    👤 ${file.uploaded_by || ""}
                </small>
            </div>
        `;

        box.appendChild(div);
    });
}

// ===================== TABS =====================
function switchTab(tab) {
    document.querySelectorAll(".section").forEach(s => s.classList.remove("active"));
    document.getElementById(tab).classList.add("active");
}

// ===================== UPLOAD =====================
function openUpload() {
    document.getElementById("uploadModal").classList.remove("hidden");
}

function closeUpload() {
    document.getElementById("uploadModal").classList.add("hidden");
}

function bgClose(e) {
    if (e.target.id === "uploadModal") closeUpload();
}

async function uploadFile(e) {
    e.preventDefault();

    const formData = new FormData(e.target);

    await fetch("/upload", {
        method: "POST",
        body: formData
    });

    closeUpload();
    loadGallery();
    loadMyGallery();

    e.target.reset();
    document.getElementById("preview").style.display = "none";
}

// ===================== VIEW =====================
async function openView(id) {
    const res = await fetch(`/file_meta/${id}`);
    const file = await res.json();

    currentFile = file;

    document.getElementById("viewImg").src = file.url;
    document.getElementById("viewModal").classList.remove("hidden");

    document.getElementById("meta").innerHTML = `
    <b>${file.title || ""}</b><br>
    ${file.description || ""}<br><br>

    📅 ${file.created_at || ""}<br>
    👤 Uploaded by: ${file.uploaded_by || ""}<br>
    🎨 Creator: ${file.creator || ""}<br>
    🏷 Tags: ${(file.tags || []).join(", ")}
`;

    document.getElementById("editTitle").value = file.title || "";
    document.getElementById("editDesc").value = file.description || "";
    document.getElementById("editCreator").value = file.creator || "";
    document.getElementById("editTags").value = (file.tags || []).join(", ");
}

function closeView() {
    document.getElementById("viewModal").classList.add("hidden");
}

function bgCloseView(e) {
    if (e.target.id === "viewModal") closeView();
}

// ===================== DELETE =====================
async function deleteFile(id) {
    await fetch(`/delete_file/${id}`, {
        method: "DELETE"
    });

    closeView();
    loadGallery();
    loadMyGallery();
}

// ===================== SAVE EDIT =====================
async function saveMeta() {
    await fetch("/update_file", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            id: currentFile.id,
            title: document.getElementById("editTitle").value,
            description: document.getElementById("editDesc").value,
            creator: document.getElementById("editCreator").value   // 👈 NEW
        })
    });

    closeView();
    loadGallery();
    loadMyGallery();
}

// ===================== DOWNLOAD =====================
function downloadFile() {
    if (!currentFile) return;

    const a = document.createElement("a");
    a.href = currentFile.url;
    a.download = "";
    a.click();
}

// ===================== SEARCH =====================
function filterGallery() {
    const q = document.getElementById("search").value.toLowerCase();

    document.querySelectorAll(".photo").forEach(p => {
        p.style.display = p.innerText.toLowerCase().includes(q)
            ? "block"
            : "none";
    });
}

// ===================== PREVIEW =====================
function previewImage(event) {
    const img = document.getElementById("preview");
    img.src = URL.createObjectURL(event.target.files[0]);
    img.style.display = "block";
}
