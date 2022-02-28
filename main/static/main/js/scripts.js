// displays the ticket-image before submitting the form
const file = document.getElementById("id_image");
if (file) {
  file.addEventListener("change", (event) => {
    const image = event.target.files[0];
    let img = document.getElementById("ticket-image");
    img.src = URL.createObjectURL(image);
    let uploadButton = document.getElementById("uploadImage");
    if (uploadButton.innerHTML === "Upload File") {
      uploadButton.innerHTML = "Upload New File";
    }
  });
}


// Modal window setup
const delete_buttons = document.getElementsByClassName("delete-button");
for (const delete_button of delete_buttons) {
  delete_button.addEventListener("click", () => {
    const delURL = delete_button.value;
    let conf_del_btn = document.getElementById('confirmDelete-button');
    conf_del_btn.href = delURL;
    let modalContent = document.getElementById('modal-container')
    modalContent.style.visibility = "visible"
  });
}


// Modal window also closes by click outside it
let outsideModal = document.getElementById("modal-container");
let modalArea = document.querySelector(".modal");
outsideModal.addEventListener("click", (event) => {
  let isClickInside = modalArea.contains(event.target);
  if (!isClickInside) {
    document.getElementById('modalReturn-button').click();
  }
});

