import gradio as gr

def pump_power_calculator(flow_rate, head, density=1000, efficiency=0.75):
    """
    Calculate pump power in Watts
    flow_rate: m³/s
    head: meters
    density: kg/m³ (default 1000 for water)
    efficiency: decimal (default 0.75)
    """
    g = 9.81  # gravity m/s²
    try:
        efficiency = float(efficiency)
        if efficiency <= 0 or efficiency > 1:
            return "Efficiency must be between 0 and 1 (decimal)."
        power = (density * g * flow_rate * head) / efficiency
        return f"Required Pump Power: {power:.2f} Watts"
    except Exception as e:
        return f"Error: {e}"

# Gradio interface
iface = gr.Interface(
    fn=pump_power_calculator,
    inputs=[
        gr.Number(label="Flow Rate (m³/s)", value=0.01),
        gr.Number(label="Head (m)", value=10),
        gr.Number(label="Fluid Density (kg/m³, default 1000)", value=1000),
        gr.Number(label="Pump Efficiency (0-1, default 0.75)", value=0.75),
    ],
    outputs=gr.Textbox(label="Pump Power"),
    title="Pump Power Calculator",
    description="Calculate the required pump power for a given flow rate, head, density, and efficiency."
)

iface.launch()
