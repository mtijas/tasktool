function closeModal(event) {
    let modal = document.getElementById('modal');
    if (modal === null || modal === undefined) {
        return;
    }
    modal.innerHTML = '<!-- placeholder -->';
    modal.setAttribute('open', 'false');
}
