const file = document.getElementById('id_image');
  file.addEventListener("change", (event) => {
      const image = event.target.files[0];
      let img = document.getElementById('ticket-image');
      img.src = URL.createObjectURL(image)
  })