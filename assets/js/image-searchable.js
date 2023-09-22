const images = document.querySelectorAll('img');
images.forEach(image => {
    const alt = image.alt;
    const isShield = image.src.includes('img.shields.io');
    if (isShield){
        const span = document.createElement('span');
        span.innerText = alt;
        span.style.fontSize = '0px';
        image.replaceWith(image, span)       
    }
});