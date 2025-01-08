import React from 'react'
import { Link } from 'react-router-dom'

const Start = () => {
  return (
    <div>
      <div className='bg-cover bg-center bg-[url(C:\Users\shiva\UBER_FULL_PROJECT\frontend\src\pages\3Dtrafficlight.png)] h-screen pt-8 flex justify-between flex-col w-full'>
        <img className='w-16 ml-8' src="https://logos-world.net/wp-content/uploads/2020/05/Uber-Logo.png" alt="" />
        <div className='bg-white pb-7 py-4 px-4'>
            <h2 className='text-[30px] font-semibold'>Get Started with Uber</h2>
            <Link to='/Login' className='flex items-center justify-center w-full bg-black text-white py-3 rounded-lg mt-5'>Continue</Link>
        </div>
      </div>
    </div>
  )
}

export default Start
