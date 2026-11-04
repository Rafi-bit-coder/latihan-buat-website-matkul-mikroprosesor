const section = document.querySelectorAll(".materi");
const navLinks = document.getElementsByClassName("lefCon")
const edit = document.querySelector(".edit")
// const observer = new IntersectionObserver((entries) => {
//     entries.forEach((entry, i) => {
//         if(entry.intersectionRatio === 1) {
//             // entry.target.classList.add("active")
//             console.log(navLinks[i].className)
//             navLinks[i].classList.add("active")
//             edit.textContent = `navLinks ke ${i}`
//         } else {
//             // entry.target.classList.remove("active")
//             // console.log(navLinks[i].id)
//             navLinks[i].classList.remove("remove")
//         }
//         if(entry.target.id === "p02") {
//             console.log(entry.intersectionRatio)
//         }
//     })
// }, {threshold: 1});

const allLinks = (materi, lefCon) => {
    for(let i = 0; i < 18; i++) {
        
    }
}


section.forEach((e) => {
    observer.observe(e);
})