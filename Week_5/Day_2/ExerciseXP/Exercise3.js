        // Exercise 1 : Change The Article

        document.querySelector('article').lastElementChild.remove();
        let h2backgroundcolor = document.querySelector('h2');
        h2backgroundcolor.addEventListener("click", h2backgroundColorchange);
        function h2backgroundColorchange() {
            h2backgroundcolor.style.backgroundColor = 'red';
        }
        let h1fontsize = document.querySelector('h1');
        h1fontsize.addEventListener("click", h1fontsizerandomchange);
        function h1fontsizerandomchange() {
            h1fontsize.style.fontSize = Math.floor(Math.random() * 101);
        }
        let h3Hide = document.querySelector('h3');
        h3Hide.addEventListener("click", h3Hider);
        function h3Hider() {
            h3Hide.style.display = 'none';
        }
        function boldText() {
            let paragraphs = document.querySelectorAll('p');
            for (let i = 0; i < paragraphs.length; i++) {
                paragraphs[i].style.fontWeight = "bold";
            }
        }
        function userAnswerTable() {
            let form = document.querySelector('form');
            let firstName = form.elements.fname.value;
            let lastName = form.elements.lname.value;
            let table = document.createElement("table");
            let tr = document.createElement('tr');
            let td = document.createElement('td');
            let td2 = document.createElement('td');
            td.style.border = "1px solid";
            td2.style.border = "1px solid";
            td.textContent = firstName;
            td2.textContent = lastName;
            tr.appendChild(td);
            tr.appendChild(td2);
            table.appendChild(tr);
            table.style.border = "1px solid";
            let div = document.querySelector('div');
            div.appendChild(table);
            event.preventDefault();
        }
        let paragraph2 = document.querySelectorAll('p')[1];
        paragraph2.addEventListener('mouseover', fadeOutEffect);
        function fadeOutEffect() {
            let fadeEffect = setInterval(function () {
                if (!paragraph2.style.opacity) {
                    paragraph2.style.opacity = 1;
                }
                if (paragraph2.style.opacity > 0) {
                    paragraph2.style.opacity -= 0.1;
                } else {
                    clearInterval(fadeEffect);
                }
            }, 200);
        }