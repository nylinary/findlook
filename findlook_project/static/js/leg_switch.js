window.onload = function() {
    var picList = [
       '{% static "images/adidas/trousers/Bryuki_Adicolor_Nylon_bezhevyj_H06695_01_laydown_ccexpress.png" %}',
       '{% static "images/adidas/trousers/Bryuki_Tiro_19_sinij_DT5174_01_laydown.jpg" %}',
       '{% static "images/adidas/trousers/Bryuki_Tiro_21_chernyj_GH7306_01_laydown.jpg" %}',
   ]
   function ImageShowCase(list) {
       var cur = 0;
       var img = document.getElementById('leg-pics');
       var update = function(index) {
           img.src = list[index];
       };
       var next = function() {
           cur = (cur < list.length - 1) ? (cur + 1) : 0;
       };
       var prev = function() {
           cur = (cur === 0) ? (cur = list.length - 1) : 0;
       };
       
       var bnext_leg = document.getElementById('bnext-leg');
       var bprev_leg = document.getElementById('bprev-leg');

       bnext_leg.addEventListener('click', function(e) {
           e.stopPropagation;
           next();
           update(cur);
       });

       bprev_leg.addEventListener('click', function(e){
           e.stopPropagation;
           prev();
           update(cur);
       });
   }
   ImageShowCase(picList);
};