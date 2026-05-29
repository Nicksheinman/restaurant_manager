

const logout=async ()=>{
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    return "ok"
}


export default logout