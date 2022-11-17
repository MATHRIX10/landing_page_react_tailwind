import React from 'react'

import {
 AiOutlineClose,
 AiOutlineMenu, 

} from 'react-icons/ai'

import { useState } from 'react';
import { useDebugValue } from 'react';

function Navbar() {
    const [nav,setNav] = useState(false);
    const handleNav = () => {
        setNav(!nav);

    }

  return (
    <div className='text-white flex justify-between items-center h-24 max-w-[1240px] mx-auto px-4'>
      <h1 className="w-full text-3xl font-bold text-[#00df9a]" >React</h1>
      <ul className="hidden md:flex ">
       <li className='p-4'>home</li>
       <li className='p-4'>compnay</li>
       <li className='p-4'>ressource</li>
       <li className='p-4'>about</li>
       <li className='p-4'>contact</li>
      </ul>
    
      <div onClick={handleNav} className = 'block md:hidden'>
        {!nav ? <AiOutlineClose size={20}/> : <AiOutlineMenu size={20}/>}
        
        
      </div>
      <div className={!nav ? "fixed laft-0 top-0 w-[60%] h-full border-r border-r-gray-900 bg-[#000300] ease-in-out duration-800 ":'fixed left-[-100%]'}>
      <h1 className="w-full text-3xl font-bold text-[#00df9a] m-4" >React</h1>
        <ul className='pt-24 uppercase p-4'>
        <li className='p-4 border-b border-gray-600'>home</li>
       <li className='p-4 border-b border-gray-600'>compnay</li>
       <li className='p-4 border-b border-gray-600'>ressource</li>
       <li className='p-4 border-b border-gray-600'>about</li>
       <li className='p-4 border-b border-gray-600'>contact</li> 
        </ul>
      </div>
    </div>
  )
}

export default Navbar
