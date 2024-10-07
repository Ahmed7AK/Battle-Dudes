const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
let x = 0;
const loop = () => {
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, 1000, 500);
    ctx.fillStyle = "black";
    ctx.fillRect(x, 10, 100, 100);
    x += 10;
    requestAnimationFrame(loop);
}

loop();

