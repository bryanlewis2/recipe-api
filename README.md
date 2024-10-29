# Recipe API

## Setup Instructions

Follow these steps to deploy the Recipe API on Heroku:

### Step 1: Create a Heroku Account
- Go to [Heroku's website](https://www.heroku.com) and sign up for a free account.

### Step 2: Create a New App
- After logging in, click on **"Create new app."**
- Specify a unique app name and select your preferred region.

### Step 3: Configure Environment Variables
- Navigate to the **Settings** tab of your app.
- Click on **"Reveal Config Vars."**
- Add the following environment variables with their respective values:
  - `SECRET_KEY`
  - `EMAIL_USER`
  - `EMAIL_PASSWORD`
  - `DB_USERNAME`
  - `DB_PORT`
  - `DB_PASSWORD`
  - `DB_NAME`
  - `DB_HOSTNAME`

### Step 4: Connect to GitHub
- Go to the **Deploy** tab.
- Select **"Connect to GitHub."**
- Log in to your GitHub account.

### Step 5: Select Repository
- Enter the name of the repository you wish to deploy and click **"Search."**
- Once found, click **"Connect"** to link your repository.

### Step 6: Manual Deployment
- Under **"Manual Deploy,"** choose the branch you want to deploy.
- Click **"Deploy Branch"** to start the deployment process.

### Step 7: Access Your Deployed App
- Once the deployment is complete, click the **"Open App"** button.
- Ensure that the URL provided by Heroku is added to the **`ALLOWED_HOSTS`** in your application's settings for it to be accessible.

