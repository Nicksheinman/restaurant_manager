import { useState } from 'react'
import loginCustomerApi from '../../api/axios/auth/login';


const LoginForm = () => {
    const [username, setUsername]= useState("testuser");
    const [password, setPassword]= useState("1234567");


    const login=async (e)=>{
        e.preventDefault()
        const response=await loginCustomerApi(username,password)
    }
    


  return (
        <form onSubmit={login} >
            <input type="text" placeholder='username' onChange={e=>{setUsername(e.target.value)}} value={username}/>
            <input type="password" placeholder='password' onChange={e=>{setPassword(e.target.value)}} value={password}/>
            <button type="submit" >submit</button>
        </form>
  )
}

export default LoginForm