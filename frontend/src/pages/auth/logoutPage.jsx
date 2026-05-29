import { redirect } from "react-router-dom"
import logout from "../../api/axios/auth/logout"
import { useEffect } from "react"
import { useNavigate } from "react-router-dom"

const LogoutPage = () => {
  const navigate = useNavigate();

  useEffect(()=>{
    const logoutEffect=async ()=>{
        await logout()
        navigate('/login')
    }
    logoutEffect()
  },[])

  return (
    <div>logoutPage</div>
  )
}

export default LogoutPage