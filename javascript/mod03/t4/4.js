'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

students.forEach(student => {
    let studentOption = document.createElement("option");
    studentOption.value = student["id"];
    studentOption.innerText = student["name"];
    document.getElementById("target").appendChild(studentOption)
});