// Login: /login/
function login() {
    let formData = new FormData()
    formData.append("username", "niklasburg")
    formData.append("password", "Sommer01")


    let response = await fetch("/login/", {
        method: "POST",
        body: formData
    })
    let result = await response.json()
    console.log("Response", result);
}

// Register: /register/
function register() {
    let formData = new FormData()
    formData.append("username", "Horst")
    formData.append("password", "Sommer01")
    formData.append("password_repeat", "Sommer01")
    formData.append("email", "Horst@gmail.com")
    formData.append("first_name", "Horst")
    formData.append("last_name", "Seehofer")


    let response = await fetch("/register/", {
        method: "POST",
        body: formData
    })
    let result = await response.json()
    console.log("Response", result);
}

// Get Boards /board/
function getBoards() {
    let token = "Token e3ea2745c300cfda21680485eaaa8b191ab2b0db"

    let response = await fetch("/board/", {
        method: "GET",
        headers: {
            Authorization: token
        }
    })
    let result = await response.json()
    console.log("Response", result);
}

// Get Tasks of Board: /task/

function getTasks() {
    let token = "Token e3ea2745c300cfda21680485eaaa8b191ab2b0db"

    let response = await fetch("/task/?board_id=2", {
        method: "GET",
        headers: {
            Authorization: token
        }
    })
    let result = await response.json()
    console.log("Response", result);
}

// Add Board: /board/add/
function addBoard() {
    let token = "Token e3ea2745c300cfda21680485eaaa8b191ab2b0db"

    let formData = new FormData()
    formData.append("name", "Horst")



    let response = await fetch("/board/add/", {
        method: "POST",
        headers: {
            Authorization: token
        },
        body: formData
    })
    let result = await response.json()
    console.log("Response", result);
}

// Add Task: /task/add/
function addTask() {
    let token = "Token e3ea2745c300cfda21680485eaaa8b191ab2b0db"

    let formData = new FormData()
    formData.append("title", "Lernen")
    formData.append("urgency", "dringend")
    formData.append("category", "testing")
    formData.append("user_id", 1)
    formData.append("board_id", 1)
    formData.append("color", "blue")



    let response = await fetch("/task/add/", {
        method: "POST",
        headers: {
            Authorization: token
        },
        body: formData
    })
    let result = await response.json()
    console.log("Response", result);
}
// Add User to Board: /board/add/user/
function addUserToBoard() {
    let token = "Token e3ea2745c300cfda21680485eaaa8b191ab2b0db"

    let formData = new FormData()
    formData.append("board_id", 3)
    formData.append("user_ids", [3])



    let response = await fetch("/board/add/user/", {
        method: "POST",
        headers: {
            Authorization: token
        },
        body: formData
    })
    let result = await response.json()
    console.log("Response", result);
}

// Get all Users from Board: /task/user/
function getUsersFromBoard() {
    //Get the Token of authenticated User: 
    let token = "Token e3ea2745c300cfda21680485eaaa8b191ab2b0db"

    let response = await fetch("/task/user/?board_id=2", {
        method: "GET",
        headers: {
            Authorization: token
        }
    })
    let result = await response.json()
    console.log("Response", result);
}

// Get all Users not in the Board: /board/user/
function getUsersNotAddedToBoard() {
    let token = "Token e3ea2745c300cfda21680485eaaa8b191ab2b0db"

    let response = await fetch("/board/user/?board_id=2", {
        method: "GET",
        headers: {
            Authorization: token
        }
    })
    let result = await response.json()
    console.log("Response", result);
}


// Remove a User from the Board: /board/remove/user/

function removeUserFromBoard() {
    let token = "Token e3ea2745c300cfda21680485eaaa8b191ab2b0db"

    let formData = new FormData()
    formData.append("board_id", 3)
    formData.append("user_ids", [3])



    let response = await fetch("/board/remove/user/", {
        method: "POST",
        headers: {
            Authorization: token
        },
        body: formData
    })
    let result = await response.json()
    console.log("Response", result);
}