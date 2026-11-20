const b=document.querySelector('.menu-btn'),n=document.getElementById('nav');
if(b&&n){b.addEventListener('click',()=>{const o=n.classList.toggle('open');b.setAttribute('aria-expanded',o);b.setAttribute('aria-label',o?'Close menu':'Open menu')});
n.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{n.classList.remove('open');b.setAttribute('aria-expanded',false)}));}
const sec=document.getElementById('memberships');
if(sec){sec.querySelectorAll('.tg').forEach(t=>t.addEventListener('click',()=>{sec.dataset.bill=t.dataset.bill;sec.querySelectorAll('.tg').forEach(x=>{const on=x===t;x.classList.toggle('on',on);x.setAttribute('aria-pressed',on)})}));}
