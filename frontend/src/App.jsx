import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import { Route, Routes } from "react-router-dom";
import RegistrationPage from './pages/auth/RegistrationPage'
import ConfirmationPage from './pages/auth/confirmationPage'
import LoginPage from './pages/auth/loginPage'

function App() {
  const [count, setCount] = useState(0)

  return (
    <Routes>
      <Route path='/registration' element={<RegistrationPage/>}/>
      <Route path='/confirmation' element={<ConfirmationPage/>}/>
      <Route path='/login' element={<LoginPage/>}/>
    </Routes>
  )
}

export default App
