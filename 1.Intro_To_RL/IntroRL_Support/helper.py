from IPython.display import HTML
import numpy as np

def HTML_print(array, color_indices, color='red', spacing=15):
    table_html = "<table>"
    for i, row in enumerate(array):
        row_html = "<tr>"
        for j, val in enumerate(row):
            cell_color = color if (i, j) in color_indices else 'black'
            cell_html = f"<td style='color: {cell_color}; text-align: center;'>{val}</td>"
            row_html += cell_html
        row_html += "</tr>"
        table_html += row_html
    table_html += "</table>"

    display(HTML(table_html))

# Example usage
array_2d = np.array([[1, 2, 3], [4, np.nan, 6], [7, 8, 9]])
color_indices = [(1, 1), (2, 2)]  # List of indices to color (row, column)

# Example usage with larger spacing
HTML_print(array_2d, color_indices)

def fill_grid(grid, array):
    if not isinstance(grid, np.ndarray) or not isinstance(array, np.ndarray):
        raise ValueError("Both inputs must be numpy arrays.")

    if (~np.isnan(grid_world.grid)).sum() != len(array):
        raise ValueError("The number of non-NaN elements in the 2D array must match the length of the 1D array.")

    filled_grid = deepcopy(grid_world.grid)
    filled_grid[~np.isnan(grid_world.grid)] = array

    return filled_grid

def pp_immediate_rewards(env):
    """
    Pretty Print the immediate rewards
    """
    rewards = fill_grid(env.grid, env.immediate_rewards)
    HTML_print(rewards, [])

def pp_state_transitions(env, state, action):
    st = fill_grid(env.grid, env.state_transitions[state, action])
    HTML_print(st, [tuple(np.argwhere(env.grid == state)[0])])