window.onload = function() {
    var image = document.getElementById('leg-pics')[0],
        imgLegDiv= document.getElementsByClassName('leg-clothes'),
        dragImgMouseStart = {},
        lastDiff = {x: 0, y: 0},
        initialPos = image.getBoundingClientRect(),
        currentPos = {x: -initialPos.width/2, y: 0};


    function mousedownDragImg(e) {
        e.preventDefault();
        dragImgMouseStart.x = e.clienX;
        dragImgMouseStart.y = e.clienY;
        currentPos.x = lastDiff.x;
        currentPos.y = lastDiff.y;
        lastDiff = {x: 0, y: 0}
        window.addEventListener('mousemove', mousemoveDragImg);
        window.addEventListener('mouseup', mouseupDragImg);
    }

    function mousemoveDragImg(e) {
        e.preventDefault();
        lastDiff.x = e.clienX - dragImgMouseStart.x;
        lastDiff.y = e.clienY - dragImgMouseStart.y;
        requestAnimationFrame(function(){
            image.style.transform = 'translate(' + (currentPos.x + lastDiff.x) + 'px,' + (currentPos.y + lastDiff.y) + 'px)';
        });
    }

    function mouseupDragImg(e) {
        e.preventDefault();
        window.removeEventListener('mousemove', mousemoveDragImg);
        window.removeEventListener('mouseup', mouseupDragImg);
    }

    image.addEventListener('mousedown', mousedownDragImg);
};