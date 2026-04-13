# Deploying SurfTheTurf to Render

This guide will help you deploy your SurfTheTurf Django application to Render.

## Prerequisites

- GitHub account with the project repository
- Render account (free tier available)
- Environment variables ready

## Step 1: Push to GitHub

First, ensure all files are committed and pushed to GitHub:

```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

## Step 2: Create a Render Account

Visit [render.com](https://render.com) and sign up with your GitHub account.

## Step 3: Connect Your GitHub Repository

1. Log in to Render Dashboard
2. Click "New +" → "Web Service"
3. Select "Build and deploy from a Git repository"
4. Connect your GitHub account and select the `SurfTheTurf` repository
5. Click "Connect"

## Step 4: Configure the Web Service

Fill in the following details:

| Setting | Value |
|---------|-------|
| **Name** | surftheturf |
| **Environment** | Python 3 |
| **Region** | Choose closest to your users |
| **Branch** | main |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn surftheturf.wsgi:application` |
| **Plan** | Free (or Starter if you want better performance) |

**Important:** Leave Build Command as shown above. Render will use the `Procfile`'s release phase to handle migrations and static file collection automatically.

### What the Procfile Does

The `Procfile` in your project includes:
- **release phase:** Runs migrations and collects static files before each deployment
- **web process:** Starts the Gunicorn server

This ensures your database is up-to-date and static files are ready whenever you deploy.

## Step 5: Add Environment Variables

Click "Advanced" and add the following environment variables:

### Required Variables

1. **SECRET_KEY** - Generate a new Django secret key
   - Visit: https://djecrety.ir/ to generate a secure key
   - Copy the generated key

2. **DEBUG** - Set to `False` for production
   ```
   False
   ```

3. **ALLOWED_HOSTS** - Your Render domain
   ```
   yourdomain.onrender.com,www.yourdomain.onrender.com
   ```

### Optional Variables

4. **DATABASE_URL** - PostgreSQL connection string (if using PostgreSQL)
   - Render will provide this if you attach a PostgreSQL database

5. **EMAIL_HOST_USER** - Your Gmail address
   ```
   your-email@gmail.com
   ```

6. **EMAIL_HOST_PASSWORD** - Gmail app password
   - See: https://support.google.com/accounts/answer/185833

7. **CSRF_TRUSTED_ORIGINS** - CSRF validation origins
   ```
   https://yourdomain.onrender.com
   ```

## Step 6: Deploy

Click "Create Web Service" to start the deployment.

Monitor the deployment:
- Check the "Logs" tab for any errors
- Wait for "All checks passed" message
- Your app should be live at: `https://yourdomain.onrender.com`

## Step 7: Post-Deployment

### Create a Superuser

Once deployed, run:

```bash
# In Render dashboard, click "Shell" in the service page
python manage.py createsuperuser
```

### Collect Static Files

This is handled automatically in the build.sh script. If you need to run it manually:

```bash
python manage.py collectstatic --noinput
```

## Troubleshooting

### Issue: "Build failed - ./build.sh: No such file or directory"

**Solution:** 
1. Go to your Render dashboard
2. Select your `surftheturf` service
3. Click **Settings** → **Build & Deploy**
4. Change the **Build Command** to: `pip install -r requirements.txt`
5. Click **Save**
6. Click **Manual Deploy** to redeploy

The migrations will run automatically via the `Procfile` release phase.

### Issue: "Module not found" errors

**Solution:** Check that all dependencies are in `requirements.txt`

```bash
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update requirements"
git push origin main
```

### Issue: Static files not loading

**Solution:** Clear the build cache and redeploy:
- In Render Dashboard → Service → Settings → Delete Build Pile

### Issue: Database errors

**Solution:** 
1. Attach a PostgreSQL database in Render
2. Render will provide DATABASE_URL automatically
3. Run migrations: `python manage.py migrate`

## Useful Commands in Render Shell

```bash
# Create superuser
python manage.py createsuperuser

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Check Django setup
python manage.py check
```

## Updating Your App

To update your deployed app:

1. Make changes locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Your update message"
   git push origin main
   ```
3. Render will automatically redeploy your app

## Monitoring

- Check logs in Render Dashboard for errors
- Monitor performance metrics in the dashboard
- Set up email alerts for deployment failures

## Additional Resources

- [Render Django Documentation](https://render.com/docs/deploy-django)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/)
- [Render Environment Variables](https://render.com/docs/environment-variables)

---

For more help, visit the Render documentation or check the deployment logs in your Render dashboard.
