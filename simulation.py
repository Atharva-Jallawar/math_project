import numpy as np
import matplotlib.pyplot as plt

def calculate_radial_heat_transfer(r1, r2, k, L, T1, T2):
    """
    Calculates steady-state radial heat transfer through a cylindrical wall.
    Formula: Q = (2 * pi * k * L * (T1 - T2)) / ln(r2 / r1)
    """
    dT = T1 - T2
    ln_ratio = np.log(r2 / r1)
    Q = (2 * np.pi * k * L * dT) / ln_ratio
    return Q

def plot_temperature_profile(r1, r2, k, L, T1, T2, Q):
    """
    Plots the exact logarithmic temperature profile across the radius.
    Formula: T(r) = T1 - (Q * ln(r / r1)) / (2 * pi * k * L)
    """
    # Generate continuous radial positions from r1 to r2
    r_coords = np.linspace(r1, r2, 200)
    
    # Analytical temperature distribution formula
    T_coords = T1 - (Q * np.log(r_coords / r1)) / (2 * np.pi * k * L)
    
    # Configure high-end scientific plotting style
    plt.style.use('dark_background')
    plt.figure(figsize=(9, 5.5))
    
    # Plot the curve with a subtle thermal color accent
    plt.plot(r_coords, T_coords, color='#facc15', linewidth=2.5, label='Temperature T(r)')
    
    # Highlight boundary points
    plt.scatter([r1, r2], [T1, T2], color=['#ef4444', '#3b82f6'], zorder=5, s=60)
    plt.text(r1 + (r2-r1)*0.02, T1, f'T1 = {T1}°C', color='#ef4444', fontweight='bold')
    plt.text(r2 - (r2-r1)*0.12, T2 + (T1-T2)*0.02, f'T2 = {T2}°C', color='#3b82f6', fontweight='bold')
    
    # Formatting
    plt.title('Logarithmic Temperature Profile Across Cylindrical Wall', fontsize=14, pad=15, fontweight='semibold')
    plt.xlabel('Radius Vector (r in cm)', fontsize=11, labelpad=8)
    plt.ylabel('Temperature (°C)', fontsize=11, labelpad=8)
    plt.grid(True, linestyle='--', alpha=0.15)
    
    # Annotate calculation telemetry
    telemetry_text = f'Geometry Parameters:\n• r1 = {r1} cm\n• r2 = {r2} cm\n• L = {L} cm\n\nThermal Matrix Result:\n• Q = {Q:.4f} cal/sec'
    plt.gca().text(0.65, 0.65, telemetry_text, transform=plt.gca().transAxes, 
                   bbox=dict(facecolor='#16161a', edgecolor='#222227', boxstyle='round,pad=1'),
                   fontsize=10, fontfamily='monospace', verticalalignment='top')
    
    plt.tight_layout()
    plt.savefig('thermal_profile_plot.png', dpi=300)
    print("[SUCCESS] Analytical thermal matrix plot saved as 'thermal_profile_plot.png'.")
    plt.show()

if __name__ == "__main__":
    # Standard engineering test configuration parameters
    r1_input = 10.0      # Inner Radius (cm)
    r2_input = 18.0      # Outer Radius (cm)
    k_input = 0.0003     # Thermal Conductivity Constant (cal/cm·s·°C)
    L_input = 100.0      # Length parameter (cm)
    T1_input = 300.0     # Inner temperature boundary (°C)
    T2_input = 400.0     # Outer temperature boundary (°C) - handles absolute delta automatically
    
    # Compute the steady-state value
    Q_resolved = calculate_radial_heat_transfer(r1_input, r2_input, k_input, L_input, T1_input, T2_input)
    
    print("="*60)
    print("        RADIAL CONDUCTION MATRIX RESOLUTION ENGINE")
    print("="*60)
    print(f"Computed Steady-State Heat Flow Rate (Q): {Q_resolved:.6f} cal/sec")
    print("="*60)
    
    # Generate the visualization graph
    plot_temperature_profile(r1_input, r2_input, k_input, L_input, T1_input, T2_input, Q_resolved)
