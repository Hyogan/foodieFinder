function initializeCarousel(carouselId, nextButtonId, prevButtonId) {
    const carousel = document.querySelector(`#${carouselId}`);
    const nextButton = document.getElementById(nextButtonId);
    const prevButton = document.getElementById(prevButtonId);
  
    nextButton.addEventListener('click', () => {
      carousel.scrollLeft += carousel.offsetWidth;
    });
  
    prevButton.addEventListener('click', () => {
      carousel.scrollLeft -= carousel.offsetWidth;
    });
  
    const checkScrollEnd = () => {
      const maxScrollLeft = carousel.scrollWidth - carousel.offsetWidth;
      if (carousel.scrollLeft === maxScrollLeft) {
        nextButton.style.cursor = 'not-allowed';
        nextButton.disabled = true;
        nextButton.classList.remove('hover:bg-slate-600');
      } else {
        nextButton.disabled = false;
        nextButton.style.cursor = 'pointer';
        nextButton.classList.add('hover:bg-slate-600');
      }
  
      if (carousel.scrollLeft === 0) {
        prevButton.disabled = true;
        prevButton.style.cursor = 'not-allowed';
        prevButton.classList.remove('hover:bg-slate-600');
      } else {
        prevButton.disabled = false;
        prevButton.style.cursor = 'pointer';
        prevButton.classList.add('hover:bg-slate-600');
      }
    };
  
    setInterval(() => {
      checkScrollEnd();
    }, 0);
  }
  
  // Usage example:
  initializeCarousel('food-carousel-item', 'food-scroll-next', 'food-scroll-prev');
  initializeCarousel('restaurants-carousel-item', 'restaurant-scroll-next', 'restaurant-scroll-prev');
  initializeCarousel('restaurants-all-carousel-item', 'restaurant-all-scroll-next', 'restaurant-all-scroll-prev');