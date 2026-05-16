import api  from "../../api";



const confirmationCustomerApi= async (token) => {
    try {
            const response=api.post("/auth/registration_Confirmation/", {token:token})
            return response
    }
    catch {
        const data = error.response.data;
        return data
    }
}

export default confirmationCustomerApi