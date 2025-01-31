# Video Game Management System

This project is a video game management system that allows users to rent, return, search, and manage video games. It includes functionalities for handling game rentals, returns, searching for games, and inventory pruning based on rental frequency and feedback ratings.

## Project Structure

- `gameRent.py`: Handles game rentals.
- `gameReturn.py`: Manages game returns and feedback submission.
- `gameSearch.py`: Provides search functionality for games based on title, genre, or platform.
- `inventoryPruning.py`: Analyzes and visualizes game rentals and feedback to suggest games for removal.
- `database.py`: Provides simple database functionalities for accessing and modifying records.
- `menu.ipynb`: Jupyter Notebook for the user interface.
- `Game_Feedback.txt`: Stores feedback for games.
- `Game_Info.txt`: Contains information about the games.
- `Rental.txt`: Records rental transactions.
- `Subscription_Info.txt`: Contains subscription information for customers.

## How to Run

1. **Clone the Repository**

   ```sh
   git clone https://github.com/gwmanthorp/video-game-management.git
   cd video-game-management
   ```

2. **Install Dependencies**
   Ensure you have Python and Jupyter Notebook installed. Install required Python packages using:

   ```sh
   pip install ipywidgets matplotlib notebook
   ```

3. **Run the Jupyter Notebook**
   Open the Jupyter Notebook to access the user interface:

   ```sh
   jupyter notebook
   ```

   Then open menu.ipynb and use the interface buttons for the following.

4. **Use the Interface**
   - **Search**: Search for games by title, genre, or platform.
   - **Rent**: Rent a game by providing customer ID and game ID.
   - **Return**: Return a rented game by providing the game ID and optionally submit feedback.
   - **Inventory Pruning**: Analyze rental frequency and feedback to identify games for removal.

## Testing

Each module contains a `test_function` that can be uncommented and run to perform basic tests on the functionalities.
