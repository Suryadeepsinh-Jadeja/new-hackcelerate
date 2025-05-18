import React from 'react';
import { motion } from 'framer-motion';

const LoadingAnimation: React.FC = () => {
  return (
    <div className="fixed inset-0 flex items-center justify-center z-50 bg-black/70 backdrop-blur-md">
      <div className="relative w-64 h-64 flex items-center justify-center">
        {/* Outer rotating ring */}
        <motion.div 
          className="absolute w-64 h-64 border-4 border-transparent border-t-blue-500 border-r-blue-400/70 rounded-full"
          animate={{ rotate: 360 }}
          transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
        />
        
        {/* Middle rotating ring */}
        <motion.div 
          className="absolute w-48 h-48 border-4 border-transparent border-t-blue-600 border-r-blue-400/50 rounded-full"
          animate={{ rotate: -360 }}
          transition={{ duration: 3, repeat: Infinity, ease: "linear" }}
        />
        
        {/* Inner rotating ring */}
        <motion.div 
          className="absolute w-32 h-32 border-4 border-transparent border-t-blue-500 border-r-blue-400/70 rounded-full"
          animate={{ rotate: 360 }}
          transition={{ duration: 1.5, repeat: Infinity, ease: "linear" }}
        />
        
        {/* Pulsing core */}
        <motion.div 
          className="absolute w-16 h-16 bg-blue-500 rounded-full"
          animate={{ scale: [1, 1.2, 1], opacity: [0.7, 1, 0.7] }}
          transition={{ duration: 2, repeat: Infinity }}
        />

        {/* Scanning lines */}
        <motion.div
          className="absolute w-full h-1 bg-gradient-to-r from-transparent via-blue-500/70 to-transparent"
          animate={{ 
            y: [-32, 32],
            opacity: [0, 1, 0]
          }}
          transition={{ 
            y: { duration: 1.5, repeat: Infinity, repeatType: "reverse" },
            opacity: { duration: 1.5, repeat: Infinity, repeatType: "reverse" }
          }}
        />

        {/* Text */}
        <div className="absolute -bottom-16 text-center">
          <div className="text-blue-400 font-mono text-lg font-bold mb-2">PROCESSING</div>
          <motion.div 
            className="flex space-x-2 justify-center"
            animate={{ opacity: [0.5, 1, 0.5] }}
            transition={{ duration: 1.5, repeat: Infinity }}
          >
            <span className="w-2 h-2 bg-blue-500 rounded-full"></span>
            <span className="w-2 h-2 bg-blue-500 rounded-full"></span>
            <span className="w-2 h-2 bg-blue-500 rounded-full"></span>
          </motion.div>
        </div>
      </div>
    </div>
  );
};

export default LoadingAnimation; 