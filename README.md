# Dodge Check

## About

Esports analytics is the application of data analysis and statistical methods to competitive video games. One of the problems in this domain is match outcome prediction. This involves using pre-game data to attempt to predict who will win. 

### What is this project? 

Dodge-Check helps you understand your chances of winning a League of Legends match before it even starts, based on which champions both teams picked.

### Why does it matter?

When you're in champion select for a ranked game, it's helpful to know if your team has a strong draft or if you're at a disadvantage. This tool analyzes the team compositions and gives you that insight - something that's actually useful for regular players, not just professionals or analysts.


# Technical Details

## Exploratory Data Analysis

The dataset that I used can be found on [Kaggle](https://www.kaggle.com/datasets/nathansmallcalder/lol-match-history-and-summoner-data-80k-matches). It contains about 148,000 ranked games of League of Legends. 

These are some key findings from the dataset. 

### Class Imbalance

In League of Legends there's something known as *blue-side advantage*. The blue team generally has a 1-3% advantage for various reasons:

- Blue side gets first pick which allows them to secure the strongest meta-defining champions before red side can respond. 
- Blue side has better access to the Rift Herald and Baron Nashor. 
- The game's default camera favours a bottom-left to top-right perspective. It makes it easier for players on the blue side to percieve skill shots because they'll generally be attacked from above.

![Charts depicting class imbalance in the dataset](./images/class-imbalance.png)


So we can see that the blue-side advantage in this particular dataset is pretty massive. Despite that, this shouldn't really be an issue for the model. Here's why:

- There are a decent number of examples of both outcomes in the dataset. Class imbalance becomes problematic when there are extreme ratios, like 90-10 or 95-5. At this level it shouldn't affect the model's ability to learn patterns.
- Even if the model becomes slightly biased towards blue side, **that's how it actually is in league**. We wouldn't expect it to be unbiased.

## Frontend Application

This project now includes a beautiful React web interface:

### [Frontend](frontend/)
- **React** web application with **TypeScript**
- **Material UI** for a modern, responsive interface
- Champion selection interface for both teams
- Mock predictions with realistic blue-side advantage
- Beautiful visualizations of win probabilities
- Runs entirely in the browser - no backend required

[View Frontend Documentation](frontend/README.md)

## Quick Start

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The application will automatically open at [http://localhost:3000](http://localhost:3000)

## Features

- **Beautiful Interface**: Modern, responsive design with League of Legends-inspired theming
- **Champion Selection**: Easy-to-use autocomplete for picking champions
- **Mock Predictions**: Realistic win probability predictions simulating blue-side advantage
- **Visual Analytics**: Clear visualization of team strengths and win probabilities
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Standalone**: No backend required - perfect for demos and development

## Screenshots

### Home Page
The landing page introduces the application with feature highlights and information about how predictions work.

### Prediction Page
Select 5 champions for each team and get instant predictions on match outcomes with visual win probability displays.

## Technologies Used

### Frontend
- React 18
- TypeScript
- Material UI (MUI)
- React Router

### Data Science (Notebooks)
- Pandas
- Scikit-learn
- XGBoost
- Jupyter Notebooks

## Project Structure

```
dodge-check/
├── frontend/               # React frontend application
│   ├── public/
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── pages/         # Page components
│   │   ├── services/      # Prediction logic
│   │   ├── data/          # Static champion data
│   │   └── types/         # TypeScript types
│   └── package.json
├── notebooks/             # Jupyter notebooks for analysis
├── data/                  # Dataset files
├── src/                   # Python utilities
└── README.md
```

## Future Enhancements

- **Backend Integration**: Connect to ML model API for real predictions
- **Champion Images**: Add visual champion portraits
- **Detailed Analysis**: Explain prediction factors and champion synergies
- **User Accounts**: Save and track prediction history
- **Live Data**: Integration with Riot Games API