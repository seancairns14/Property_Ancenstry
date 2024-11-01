const canvas = document.getElementById('gridCanvas');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let scale = 1;
let panX = 0;
let panY = 0;
const gridSize = 50;

function drawGrid() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.save();
    ctx.translate(panX, panY);
    ctx.scale(scale, scale);

    ctx.beginPath();
    for (let x = 0; x < canvas.width; x += gridSize) {
        ctx.moveTo(x, 0);
        ctx.lineTo(x, canvas.height);
    }
    for (let y = 0; y < canvas.height; y += gridSize) {
        ctx.moveTo(0, y);
        ctx.lineTo(canvas.width, y);
    }
    ctx.strokeStyle = '#ddd';
    ctx.lineWidth = 1 / scale;
    ctx.stroke();

    ctx.restore();
}

let isPanning = false;
let startX, startY;

canvas.addEventListener('mousedown', (e) => {
    isPanning = true;
    startX = e.clientX - panX;
    startY = e.clientY - panY;
});

canvas.addEventListener('mousemove', (e) => {
    if (isPanning) {
        panX = e.clientX - startX;
        panY = e.clientY - startY;
        drawGrid();
    }
});

canvas.addEventListener('mouseup', () => {
    isPanning = false;
});

canvas.addEventListener('mouseleave', () => {
    isPanning = false;
});

canvas.addEventListener('wheel', (e) => {
    e.preventDefault();
    const zoomFactor = 0.1;
    const oldScale = scale;

    if (e.deltaY < 0) {
        scale += zoomFactor;
    } else {
        scale = Math.max(0.1, scale - zoomFactor);
    }

    const mouseX = e.clientX - canvas.offsetLeft;
    const mouseY = e.clientY - canvas.offsetTop;

    panX -= (mouseX / oldScale - mouseX / scale);
    panY -= (mouseY / oldScale - mouseY / scale);

    drawGrid();
});

function addBox(x, y, width, height, color = 'blue') {
    ctx.save();
    ctx.translate(panX, panY);
    ctx.scale(scale, scale);
    ctx.fillStyle = color;
    ctx.fillRect(x, y, width, height);
    ctx.restore();
}

drawGrid();
