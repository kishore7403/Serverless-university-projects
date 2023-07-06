import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import SignInForm from "./SignInForm";
import SignUpForm from "./SignUpForm";
import DashboardPage from "./DashboardPage";

const App = () => {
  return (
    // <Router>
      <div>
        <Routes>
          <Route exec path="/" element={<SignUpForm />} />
          <Route path="/signup" element={<SignUpForm />} />
          <Route path="/signin" element={<SignInForm />} />
          <Route path="/dashboard" element={<DashboardPage />} />
        </Routes> 
        {/* [1] */}
      </div>
    // </Router>
  );
};

export default App;

//References
//[1] 	Remix Software, Inc., "<Routes>," Remix Software, Inc., [Online]. Available: https://reactrouter.com/en/main/components/routes. [Accessed 04 July 2023].