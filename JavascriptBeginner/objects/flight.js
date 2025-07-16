const departTripTicket = {
    name: "junior",
    from: "Amsterdam",
    to: "Madrid",
    businessClass: false,
    upgrade() {
        if (departTripTicket.businessClass == true) {
            console.log("You are already in business class");
        } else {
            departTripTicket.businessClass = true;
            console.log("you have now been upgrade to business class.")
        }
    }
}
const returnTripTicket = {
    name: "junior",
    from: "madrid",
    to: "amsterdam",
    businessClass: false,
    upgrade() {
        if (returnTripTicket.businessClass == true) {
            console.log("You are already in business class");
        } else {
            returnTripTicket.businessClass = true;
            console.log("you have now been upgrade to business class.")
        }
    }
}

departTripTicket.upgrade();
console.log(departTripTicket);