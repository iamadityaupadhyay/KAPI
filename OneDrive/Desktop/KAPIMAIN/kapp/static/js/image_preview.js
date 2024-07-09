document.addEventListener("DOMContentLoaded", function() {
    var imageInput = document.querySelector("[id$='adhar_images']");
    if (imageInput) {
        imageInput.addEventListener("change", function() {
            var file = this.files[0];
            if (file) {
                var reader = new FileReader();
                reader.onload = function(e) {
                    var preview = document.getElementById("image_preview");
                    if (!preview) {
                        preview = document.createElement("img");
                        preview.id = "image_preview";
                        imageInput.parentNode.insertBefore(preview, imageInput.nextSibling);
                    }
                    preview.src = e.target.result;
                    preview.style.maxWidth = "200px";
                    preview.style.maxHeight = "200px";
                    preview.style.marginTop = "10px";
                };
                reader.readAsDataURL(file);
            }
        });
    }
});