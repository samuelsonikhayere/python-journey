# My first code
# Analysing bacterial growth (OD readings) and classifying each hour into a growth phase
# Also tracks the biggest jump in OD between consecutive hours

od_readings = [0.05, 0.06, 0.09, 0.18, 0.34, 0.61, 0.95, 1.20, 1.35, 1.42, 1.44, 1.43]

def analyse_od(od_readings):

  result = {}
  phase_count = {"Lag phase": 0, "Log phase": 0, "Stationary/Decline": 0}
  max_jump = 0
  max_hour = 1

  for i, OD in enumerate (od_readings, start = 1):
    if OD < 0.1:
      phase = "Lag phase"
    elif OD < 1.0:
      phase = "Log phase"
    else:
      phase = "Stationary/Decline"

    result[i] = (OD, phase)
    phase_count[phase] += 1

    print (f"Hour: {i:>2} | OD = {OD:.2f} | {phase}")

    if i > 1:
      jump = OD - od_readings[i - 2]
      if jump > max_jump:
        max_jump = jump
        max_hour = i

  print (f"\nPhase Summary: {phase_count}")
  print (f"Maximum Jump at Hour: {max_hour} (Maximum Change in OD: {max_jump:.2f})")
  return result

analyse_od (od_readings)
