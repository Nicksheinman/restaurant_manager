import api  from "../../api";

const loginCustomerApi= async (username, password) => {
    try {
            const response=await api.post("/auth/login_user/", {username:username, password:password})
            localStorage.setItem("access", response.data.access);
            localStorage.setItem("refresh", response.data.refresh);
            return response
    }
    catch {
        const data = error.response.data;
        return data
    }
}

export default loginCustomerApi