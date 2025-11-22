// Массив с программами
const programs = [
  { name: "Blender", site: "https://www.blender.org/", version: "2.93" },
  { name: "7-Zip", site: "https://www.7-zip.org/", version: "19.00" },
  { name: "Bluestacks", site: "https://www.bluestacks.com/", version: "5.5.100" },
  { name: "Cheat Engine", site: "https://cheatengine.org/", version: "7.5" },
  { name: "Cisco Packet Tracer", site: "https://www.netacad.com/", version: "8.2.2" },
  { name: "EA App", site: "https://www.ea.com/", version: "12.0.1" },
  { name: "GitHub Desktop", site: "https://desktop.github.com/", version: "3.4.2" },
  { name: "Firefox", site: "https://www.mozilla.org/en-US/firefox/", version: "89.0" },
  { name: "Hoyolab / HoYoPlay", site: "https://www.hoyolab.com/", version: "2.0" },
  { name: "Hydra", site: "https://hydra.io/", version: "3.0.5" },
  { name: "Java 8", site: "https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html", version: "Update 441" },
  { name: "Minecraft Launcher", site: "https://www.minecraft.net/", version: "1.17" },
  { name: "Notepad++", site: "https://notepad-plus-plus.org/", version: "7.9.5" },
  { name: "Parsec", site: "https://parsec.app/", version: "1.7" },
  { name: "PuTTY", site: "https://www.putty.org/", version: "0.81" },
  { name: "Oracle VM VirtualBox", site: "https://www.virtualbox.org/", version: "7.0.18" },
  { name: "OBS Studio", site: "https://obsproject.com/", version: "27.2.4" },
  { name: "OBS-VirtualCam", site: "https://github.com/CatxFish/obs-virtual-cam", version: "2.0.4" },
  { name: "Spotify", site: "https://www.spotify.com/", version: "1.2.61.443" },
  { name: "Steam", site: "https://store.steampowered.com/", version: "2021.08.18" },
  { name: "Telegram", site: "https://telegram.org/", version: "5.13.1" },
  { name: "Viber", site: "https://www.viber.com/", version: "23.0.0.0" },
  { name: "Discord", site: "https://discord.com/", version: "1.0.9152" },
  { name: "Wacom драйвер", site: "https://www.wacom.com/", version: "-" },
  { name: "CrystalDiskInfo", site: "https://crystalmark.info/en/software/crystaldiskinfo/", version: "9.3.2" },
  { name: "CrystalDiskMark", site: "https://crystalmark.info/en/software/crystaldiskmark/", version: "8.0.5" },
  { name: "Rufus", site: "https://rufus.ie/", version: "4.5" },
  { name: "Ventoy", site: "https://www.ventoy.net/", version: "1.0.99" },
  { name: "TranslucentTB", site: "https://github.com/TranslucentTB/TranslucentTB", version: "1.0.0" },
  { name: "HyperX NGENUITY", site: "https://www.hyperxgaming.com/us", version: "5.0.0" },
  { name: "Digidoc4", site: "https://www.hyperxgassming.com/us", version: "5.0.0" },
  { name: "honkai imp", site: "https://www.hyperxgassming.com/us", version: "5.0.0" },
  { name: "afk jou", site: "https://www.hyperxgassming.com/us", version: "5.0.0" },
  { name: "ddd", site: "https://www.hyperxgassming.com/us", version: "5.0.0" },
];

// Массив с драйверами
const drivers = [
  { name: "Intel Driver & Support Assistant", photo: "" },
  { name: "LAN_Realtek Driver", photo: "" },
  { name: "Realtek Audio Driver", photo: "" },
  { name: "NVIDIA Control Panel / App", photo: "" },
  { name: "Killer Network Manager", photo: "" },
  { name: "Wacom Driver", photo: "" },
  { name: "HyperX NGENUITY", photo: "" },
  { name: "ThunderMaster", photo: "" },
  { name: "Snappy Driver Installer", photo: "" },
  { name: "SSD Mini Tweaker", photo: "" },
  { name: "Archer-T5E (Wi-Fi/Bluetooth)", photo: "" },
  { name: "Microsoft Visual C++ Redistributable", photo: "" },
];

// Картинки
const images = [
  { id: "emoji", src: "pictures/chapr/HuTao.png" },
  { id: "background", src: "pictures/wallpaper/best-zhezhi-echoes-in-wuthering-waves.avif" },
  { id: "image2", src: "pictures/7zip-icon.png" },
];

// Функция для создания строки с программой
function createProgramRow(program, index) {
  const row = document.createElement("tr");

  const checkboxCell = document.createElement("td");
  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.checked = localStorage.getItem(`program_${program.name}`) === "true";
  checkbox.addEventListener("change", () => {
    localStorage.setItem(`program_${program.name}`, checkbox.checked);
  });
  checkboxCell.appendChild(checkbox);
  row.appendChild(checkboxCell);

  const numberCell = document.createElement("td");
  numberCell.textContent = index + 1;
  row.appendChild(numberCell);

  const nameCell = document.createElement("td");
  const link = document.createElement("a");
  link.href = program.site;
  link.textContent = program.name;
  link.target = "_blank";
  nameCell.appendChild(link);
  row.appendChild(nameCell);

  const versionCell = document.createElement("td");
  versionCell.textContent = program.version;
  row.appendChild(versionCell);

  return row;
}

// Функция для создания строки с драйвером
function createDriverRow(driver, index) {
  const row = document.createElement("tr");

  const checkboxCell = document.createElement("td");
  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.checked = localStorage.getItem(`driver_${driver.name}`) === "true";
  checkbox.addEventListener("change", () => {
    localStorage.setItem(`driver_${driver.name}`, checkbox.checked);
  });
  checkboxCell.appendChild(checkbox);
  row.appendChild(checkboxCell);

  const numberCell = document.createElement("td");
  numberCell.textContent = index + 1;
  row.appendChild(numberCell);

  const nameCell = document.createElement("td");
  nameCell.textContent = driver.name;
  row.appendChild(nameCell);

  const photoCell = document.createElement("td");
  const img = document.createElement("img");
  img.src = driver.photo;
  img.alt = driver.name;
  img.style.width = "80px";
  photoCell.appendChild(img);
  row.appendChild(photoCell);

  return row;
}

// Загрузка данных при старте
window.onload = () => {
  images.forEach(image => {
    const imgElement = document.getElementById(image.id);
    if (imgElement) imgElement.src = image.src;
  });

  const programsTable = document.querySelector("#programs tbody");
  const driversTable = document.querySelector("#drivers tbody");

  programs.forEach((program, index) => {
    const row = createProgramRow(program, index);
    programsTable.appendChild(row);
  });

  drivers.forEach((driver, index) => {
    const row = createDriverRow(driver, index);
    driversTable.appendChild(row);
  });
};
