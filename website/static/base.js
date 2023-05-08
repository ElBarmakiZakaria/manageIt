
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))



function showdropdown(){
    var profile = document.getElementById("profile");
    var isclicked = profile.getAttribute("isclicked");
    var drop = document.getElementById("dropdown");
    console.log(isclicked)
    if (isclicked == 'true'){
        isclicked = profile.setAttribute("isclicked", "false");
        drop.style.top = "-10px";
        drop.style.opacity = 0 ;
        drop.style.visibility= "hidden";
        
    }else{
        isclicked =profile.setAttribute("isclicked", "true");
        drop.style.visibility= "visible";
        drop.style.top = "15px";
        drop.style.opacity = 1 ;
    }

}


const modal = document.getElementById("mymodal");
const addModal = document.getElementById("add-modal");




// const task_card = document.getElementById("card-body")

const editModal = document.getElementById("modals");
const idplace = document.getElementById("idplace")
const titleplace = document.getElementById("titleplace");
const descriptionplace = document.getElementById("descriptionplace");
const low = document.getElementById("low");
const medium = document.getElementById("medium");
const high = document.getElementById("high");
const statusPending = document.getElementById("statusPending");
const statusCompleted = document.getElementById("statusCompleted");
const dateplace = document.getElementById("dateplace")

function handleCardClick(id, title, description, priority, status, dueDate) {
    editModal.style.visibility = "visible"
    idplace.setAttribute("value", id)
    titleplace.setAttribute("value", title);
    descriptionplace.setAttribute("value", description);
    if(priority == 'Low'){
        low.setAttribute("selected", true);
    }else if(priority == 'Medium'){
        medium.setAttribute("selected", true);
    }else{
        high.setAttribute("selected", true);
    }

    if(status == 'Pending'){
        statusPending.setAttribute("checked", true);
    }else if(status == 'Completed'){
        statusCompleted.setAttribute("checked", true);
    }

    dateplace.setAttribute("value", dueDate)

    // console.log("Id: " + id);
    // console.log("Title: " + title);
    // console.log("Description: " + description);
    // console.log("Priority: " + priority);
    // console.log("Status: " + status);
    // console.log("Due date: " + dueDate);

}


modal.addEventListener("click",  function(e) {
    if (e.target === modal) {
        CloseModal();
    }
});


function OpenModal(){
    modal.style.visibility = "visible";

}
function CloseModal(){
    modal.style.visibility = "hidden";
    editModal.style.visibility = "hidden"

    
}


