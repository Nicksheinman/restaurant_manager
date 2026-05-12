import api  from "../../api";

const registerCustomerApi= async (username, password, secondPassword, email, firstName, lastName) => {
    try {
            const response=api.post("/auth/registration/", {username:username, password:password, second_password:secondPassword, email:email, first_name:firstName, last_name:lastName})
            return response
    }
    catch {
        const data = error.response.data;
        return data
    }
}

export default registerCustomerApi