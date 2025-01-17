document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("modal");
    const closeModal = document.getElementById("close-modal");

    // Show the modal on load
    setTimeout(() => {
      modal.classList.add("show");
    }, 500); // Delay to simulate loading

    // Close modal on button click
    closeModal.addEventListener("click", () => {
      modal.classList.remove("show");
    });

    // Optional: Close modal on clicking outside the content
    window.addEventListener("click", (e) => {
      if (e.target === modal) {
        modal.classList.remove("show");
      }
    });
  });