# RoomStop

A comprehensive room rental and roommate matching platform for Boston. RoomStop connects people looking for housing with available rooms and compatible roommates through intelligent matching algorithms and real-time rental data.

## Overview

RoomStop simplifies the housing search process in Boston by aggregating rental listings and matching users with compatible roommates based on lifestyle preferences, budgets, and location requirements. The platform combines real-time rental data from Zillow with a proprietary roommate matching algorithm to create optimal housing arrangements.

## System Architecture

### Frontend - React Application

Modern, responsive web interface built with React and deployed on Vercel. Provides intuitive user experience for browsing listings, managing profiles, and connecting with potential roommates.

### Backend - API Server

RESTful API service that manages data flow between all system components. Integrates with Zillow API for real-time rental listings and maintains MongoDB database for user profiles and room information. Deployed on Railway for reliable cloud hosting.

### Recommendation Engine

Machine learning module that calculates compatibility between users using cosine similarity algorithms. Analyzes user preferences, lifestyle patterns, and requirements to generate personalized roommate recommendations.

## Tech Stack

- **Frontend**: React, Tailwind CSS, Axios
- **Backend**: Node.js, Express, MongoDB
- **Recommendation System**: Python, NumPy, Scikit-learn
- **External APIs**: Zillow API
- **Deployment**: Vercel (Frontend), Railway (Backend)
