// Buka modal dan render ulang Mermaid diagram supaya tampil benar
function openModal() {
    const modal = document.getElementById("fsmModal");
    modal.style.display = "block";

    const mermaidDiv = document.getElementById("mermaidDiagram");
    if (mermaidDiv) {
        // Reset innerHTML to raw text to force re-render
        const code = mermaidDiv.textContent || mermaidDiv.innerText;
        mermaidDiv.innerHTML = code.trim();
        mermaid.init(undefined, mermaidDiv);
    }
}

// Tutup modal
function closeModal() {
    const modal = document.getElementById("fsmModal");
    modal.style.display = "none";
}

// Validasi input angka (optional)
document.querySelector('form').addEventListener('submit', function(event) {
    var value = document.getElementById('value').value;
    if (isNaN(value)) {
        alert("Please enter a valid number.");
        event.preventDefault();
    }
});
