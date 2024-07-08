const modalShow = (product) => {
  console.log(product);
  const modal = document.getElementById("modal-default");
  modal.classList.add("modalOpen");
  modal.classList.add("show");
};

const modalHide = () => {
  const modal = document.getElementById("modal-default");
  modal.classList.remove("modalOpen");
  modal.classList.remove("show");
};
