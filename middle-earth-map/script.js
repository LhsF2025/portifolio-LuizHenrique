document.getElementById("updateForm").addEventListener("submit", function(event) {
  event.preventDefault();

  const size = document.getElementById("sz").value;
  const color = document.getElementById("co").value;
  const name = document.getElementById("name").value;
  const email = document.getElementById("em").value;

  const list = document.getElementById("place-list");
  list.style.fontSize = size === "big" ? "20px" : "14px";
  list.style.color = color;

  alert(`Thanks ${name}, we'll send updates to ${email}!`);
});
