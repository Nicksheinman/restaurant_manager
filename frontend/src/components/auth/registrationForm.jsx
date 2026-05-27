import React from 'react'
import { useState } from 'react'
import registerCustomerApi from '../../api/axios/auth/register';


const RegistrationForm = () => {
    const [username, setUsername]= useState("testuser");
    const [email, setEmail]= useState("nickprojectsmail@gmail.com");
    const [password, setPassword]= useState("1234567");
    const [secondPassword, setSecondPassword]= useState("1234567");
    const [firstName, setFirstName]= useState("nick");
    const [lastName, setLastName]= useState("");

    const registration=async (e)=>{
        e.preventDefault()
        const response=await registerCustomerApi(username,password, secondPassword, email, firstName, lastName)
    }
    


  return (
        <form onSubmit={registration} >
            <input type="text" placeholder='username' onChange={e=>{setUsername(e.target.value)}} value={username}/>
            <input type="email" placeholder='email' onChange={e=>{setEmail(e.target.value)}} value={email}/>
            <input type="password" placeholder='password' onChange={e=>{setPassword(e.target.value)}} value={password}/>
            <input type="password" placeholder='password2' onChange={e=>{setSecondPassword(e.target.value)}} value={secondPassword}/>
            <input type="text" placeholder='first name' onChange={e=>{setFirstName(e.target.value)}} value={firstName}/>
            <input type="text" placeholder='last name' onChange={e=>{setLastName(e.target.value)}} value={lastName}/>
            <button type="submit" >submit</button>
        </form>
  )
}

export default RegistrationForm