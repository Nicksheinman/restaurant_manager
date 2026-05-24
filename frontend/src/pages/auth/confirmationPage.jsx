import React from 'react'
import confirmationCustomerApi from '../../api/axios/auth/confirmation'
import { useEffect } from 'react'

const ConfirmationPage = () => {
    
    useEffect( ()=>{
        const confirm=async ()=>{
            const token=new URLSearchParams(window.location.search).get('token');
            const res=await confirmationCustomerApi(token)
        }

        confirm()
    }, [])
}

export default ConfirmationPage