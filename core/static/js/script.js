// const switch_lang_btn = document.getElementById("switch_lang_btn");
const switch_lang_btn = document.querySelector(".classic .switch_lang_btn");
const toggle_block = document.querySelector(".classic #dropdown-lang");
const dropdown_content =  document.querySelector(".classic .dropdown-content");
                    // MOBILES DOM SELECTIONS
const switch_lang_btn_mobile = document.querySelector(".mobile .switch_lang_btn");
const toggle_block_mobile = document.querySelector('.mobile #dropdown-lang-mobile')
const dropdown_content_mobile =  document.querySelector(".mobile .dropdown-content");


    switch_lang_btn.addEventListener('click', (event) => {
        // alert("hello world");
        // console.log(event.target);
        toggleFunction('big_screen');
    });
    switch_lang_btn.addEventListener('focus', (event) => {
        // console.log(event.target);
        toggleFunction('big_screen');
    });

    switch_lang_btn_mobile.addEventListener('click',()=>{
        toggleFunction('mobile')
    })
    switch_lang_btn.addEventListener('focus', (event) => {
        // console.log(event.target);
        toggleFunction('mobile');
    });




// elise.addEventListener('click', ()=> {
//     alert('hello world of many things')
// })

function toggleFunction(screen_size) { 
    toggle_elements = ["px-4","py-4", "mt-4", "space-y-4","flex","hidden","h-0","h-fit"]
    toggle_elements.forEach(element => {
        if(screen_size == 'big_screen')
            dropdown_content.classList.toggle(element)
        else if(screen_size == "mobile")
            dropdown_content_mobile.classList.toggle(element)
    });
    
}

document.addEventListener("click", (event) => {
    const isClickedInside = toggle_block.contains(event.target);
    const isMobileClickedInside = toggle_block_mobile.contains(event.target);
    let flexed = false;
    if(dropdown_content.classList.contains("flex") || dropdown_content_mobile.classList.contains('flex')) 
        flexed = true;
    else 
        flexed = false;

    if(!isClickedInside && flexed) 
    {
        toggleFunction('big_screen');
    }
    if(!isMobileClickedInside && !isClickedInside && flexed){
        toggleFunction('mobile')
    }
});


    const store_lang = (event)=> {
        let new_lang = event.target.id
        new_lang = new_lang.slice(5,new_lang.length)
        // alert(new_lang)
        switch_language(new_lang);
    }
    dropdown_content.addEventListener('click', function(event) {
      // Check which button was clicked
      store_lang(event)
    });
    dropdown_content_mobile.addEventListener('click', function(event) {
        // Check which button was clicked
        store_lang(event)
      });
  

const switch_language = (lang) => {
    localStorage.setItem("lang", lang);
    
    if(localStorage.getItem('lang') == "fr")
        base_text = "Choisissez une langue"
    else if (localStorage.getItem('lang') == "en")
        base_text = "Choose a language"
    const final_text = `${base_text} (${lang})`;
    const switch_lang_text = document.querySelectorAll(".switch_lang_text");
    switch_lang_text.forEach(switch_text => {
        switch_text.textContent = final_text
    });
} 




const header = document.querySelector("#header-side");
const hamburger = document.querySelector(".hamburger");
// const navbar = document.querySelector("nav")
hamburger.addEventListener("click",()=>{
    // alert("Hellow world")

    header.classList.toggle("translate-x-full");
    header.classList.toggle("translate-x-0");
    hamburger.classList.toggle("open");
    // if(hamburger.id)

});




// CAROUSSEL COURSE

document.addEventListener('DOMContentLoaded',()=>{
    const carouselContainer = document.querySelector('.overflow-x-auto');
    const carouselItems = document.querySelector("#food-carousel");
    const firstItem = carouselItems.children[0];

    carouselItems.innerHTML += carouselItems.innerHTML;

    setInterval(() => {
        carouselContainer.scrollLeft += firstItem.offsetWidth;
    }, 3000);
});




