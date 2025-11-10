'use strict';
const names = ['John', 'Paul', 'Jones'];

names.forEach(name => {document.getElementById("target").innerHTML += "<li>" + name + "</li>";});