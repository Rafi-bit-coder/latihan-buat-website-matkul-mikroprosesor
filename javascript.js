const section = document.querySelectorAll(".materi")
const navLinks = document.querySelectorAll(".lefCon")

const observer = new IntersectionObserver(entries => {
    console.clear()
    entries.forEach(entry => {
        navLinks.forEach(a => {
            a.classList.toggle("active", entry.target.id === a.id)
        })
        // console.log(entry)
    })
}, {threshold: 1})

section.forEach(e => {
    observer.observe(e);
})