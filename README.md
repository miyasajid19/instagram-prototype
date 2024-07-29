# Instagram Prototype using Tkinter

## Overview
This project is a prototype of an Instagram-like application built using Python's Tkinter module. The application includes essential features such as user registration, login, post management, and more, resembling the core functionalities of Instagram.

## Features

1. **New Registration**
   - Register new users with a unique username, a secure password, and a valid email address.

2. **Login System**
   - Securely log in with your credentials, verifying username and password.

3. **Navbar**
   - A navigation bar provides quick access to Home, Profile, Add Post, and other essential features.

4. **Add Post**
   - Create and upload new posts, including images and captions.

5. **Update Post**
   - Edit existing posts to change images or captions.

6. **Delete Post**
   - Permanently remove posts from the database.

7. **Like/Unlike Post**
   - Like and unlike posts with visible like counts.

8. **Comment on Post**
   - Add comments to posts, displayed below each post.

9. **View Specific User's Posts**
   - View all posts from a specific user in a well-organized layout.

10. **Update Account**
    - Update your account details such as Name, password, and email. However, cannot upate their mail and username.

11. **Password Recovery**
    - Recover passwords unsecurely through just username.

## Current Limitations

1. **Lack of Validation**
   - Input fields currently do not validate data, which may lead to invalid entries.

2. **Inability to Delete Comments**
   - Users cannot delete comments once posted.
3. **forget password**
   - its easy to snoop to others account as there is no validation for recovering password
## Future Enhancements

1. **Implement Input Validation**
   - Add validation to ensure accurate and safe data entry during registration and login.

2. **Enable Comment Deletion**
   - Allow users to delete their comments.

3. **Enhance User Interface**
   - Improve the visual design and layout for a better user experience.

4. **Security Enhancements**
   - Implement stronger security measures to protect user data.

5. **Performance Optimization**
   - Optimize the application to efficiently handle large amounts of data and users.
6. **validation**
  - using smtplib module we can easily validate the mail used for registration
  - the account can be made more secure via providing otp in the registerred account mail
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/miyasajid19/instagram-prototype.git
2. Change to .exe file
   ```bash
   pyinstaller  index.py --onefile --noconsole



## Usage

### Registering a New Account
1. Open the application.
2. Navigate to the **Register** option from the navigation bar or the initial screen.
3. Fill in the required fields:
   - **Username**: Enter a unique username.
   - **Password**: Choose a strong password.
   - **Email**: Provide a valid email address.
4. Click on the **Register** button to create your account.
5. A confirmation message will appear if the registration is successful.

### Logging In
1. Open the application.
2. Navigate to the **Login** option from the navigation bar or the initial screen.
3. Enter your registered **Username** and **Password**.
4. Click on the **Login** button to access your account.
5. Upon successful login, you will be redirected to the home screen.

### Exploring Features
- **Home**: View a feed of posts from all users.
- **Profile**: Access your profile to view your posts and account information.
- **Add Post**:
  1. Click on the **Add Post** button in the navigation bar.
  2. Select an image and add a caption.
  3. Click on the **Post** button to share your post.
- **Update Post**:
  1. Navigate to the post you want to update.
  2. Click on the **Edit** button.
  3. Make the necessary changes to the image and/or caption.
  4. Save the changes.
- **Delete Post**:
  1. Navigate to the post you want to delete.
  2. Click on the **Delete** button.
  3. Confirm the deletion to remove the post permanently.

### Liking and Commenting on Posts
- **Like a Post**:
  1. Navigate to the post you want to like.
  2. Click on the **Like** button below the post.
  3. The like count will update accordingly.
- **Unlike a Post**:
  1. If you have already liked a post, click on the **Unlike** button to remove your like.
- **Comment on a Post**:
  1. Navigate to the post you want to comment on.
  2. Enter your comment in the comment box below the post.
  3. Click on the **Comment** button to add your comment.

### Managing Account Information
- **Update Account Information**:
  1. Go to your **Profile**.
  2. Click on the **Update Account** button.
  3. Modify your username, password, and/or email.
  4. Save the changes.

### Recovering Password
1. On the login screen, click on the **Forgot Password?** link.
2. Enter your registered email address.
3. Follow the instructions sent to your email to reset your password.

## Contributing
We welcome contributions to improve this project! Here’s how you can contribute:

1. **Fork the Repository**:
   - Navigate to the project repository on GitHub.
   - Click on the **Fork** button at the top-right corner to create a copy of the repository on your GitHub account.

2. **Clone Your Fork**:
   - Open your terminal or command prompt.
   - Clone your forked repository to your local machine using the following command:
     ```bash
     https://github.com/miyasajid19/instagram-prototype.git
     ```
.

3. **Create a New Branch**:
   - Navigate to the project directory:
     ```bash
     cd instagram-prototype-tkinter
     ```
   - Create a new branch for your feature or bug fix:
     ```bash
     git checkout -b feature-name
     ```
   - Replace `feature-name` with a descriptive name for your branch.

4. **Make Your Changes**:
   - Implement your feature or bug fix.
   - Ensure your code follows the project’s coding standards.

5. **Commit Your Changes**:
   - Add your changes to the staging area:
     ```bash
     git add .
     ```
   - Commit your changes with a descriptive commit message:
     ```bash
     git commit -m "Description of the feature or bug fix"
     ```

6. **Push Your Changes**:
   - Push your branch to your forked repository:
     ```bash
     git push origin feature-name
     ```

7. **Create a Pull Request**:
   - Navigate to the original project repository on GitHub.
   - Click on the **Pull Requests** tab.
   - Click on the **New Pull Request** button.
   - Select your branch from the drop-down menu.
   - Add a descriptive title and detailed description for your pull request.
   - Click on the **Create Pull Request** button.

We will review your pull request and provide feedback. Once approved, your changes will be merged into the main repository.

Thank you for contributing!



#interfaces

![Screenshot 2024-07-29 012649](https://github.com/user-attachments/assets/a0160575-51ae-4bde-9cec-333efaa27898)

![Screenshot 2024-07-29 012747](https://github.com/user-attachments/assets/0e948aab-a8a6-4404-81be-9d1e9a82ebe2)

![Screenshot 2024-07-29 012804](https://github.com/user-attachments/assets/a2bdd5f2-024b-44aa-8b57-599d8bc88abc)

![Screenshot 2024-07-29 012822](https://github.com/user-attachments/assets/b3608ecf-d449-42bd-be0f-c8e128430236)

![Screenshot 2024-07-29 012945](https://github.com/user-attachments/assets/3d6a7208-f3d6-49a6-83c2-58d34b5a2aa8)

![Screenshot 2024-07-29 012957](https://github.com/user-attachments/assets/82ee6d86-d1d4-40bf-ba94-6f59a48f2cb4)

![Screenshot 2024-07-29 013008](https://github.com/user-attachments/assets/bd427dc3-b7d0-4df1-b2d9-314c6fd89931)

![Screenshot 2024-07-29 013110](https://github.com/user-attachments/assets/38d17fc3-5500-4ec2-8755-a19bfdb69e9e)

![Screenshot 2024-07-29 013253](https://github.com/user-attachments/assets/ab06df23-52f3-4f66-be7f-a726975185fa)

![Screenshot 2024-07-29 013331](https://github.com/user-attachments/assets/88607162-1d05-4c20-9aa8-6a88c9ae2b8b)

![Screenshot 2024-07-29 013341](https://github.com/user-attachments/assets/d45b43ca-7db7-4953-b1cd-9ffe89bbf1c5)

![Screenshot 2024-07-29 013627](https://github.com/user-attachments/assets/801a5760-eabe-4413-9fc9-b64034ad6416)


