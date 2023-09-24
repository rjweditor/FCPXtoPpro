import timelinio
import os

def convert_fcpxml_to_premiere(fcpxml_file, premiere_file):
  """Converts a Final Cut Pro X XML file to an Adobe Premiere XML file.

  Args:
    fcpxml_file: The path to the Final Cut Pro X XML file.
    premiere_file: The path to the output Adobe Premiere XML file.
  """

  # Create a TimelineIO project.
  project = timelinio.Project()

  # Import the Final Cut Pro X XML file.
  project.import_fcpxml(fcpxml_file)

  # Export the project as an Adobe Premiere XML file.
  project.export_premiere_xml(premiere_file)

if __name__ == '__main__':
  # Get the path to the Final Cut Pro X XML file.
  fcpxml_file = input('Enter the path to the Final Cut Pro X XML file: ')

  # Get the path to the output Adobe Premiere XML file.
  premiere_file = input('Enter the path to the output Adobe Premiere XML file: ')

  # Convert the file.
  convert_fcpxml_to_premiere(fcpxml_file, premiere_file)

  # Print a success message.
  print('The Final Cut Pro X XML file has been converted to an Adobe Premiere XML file.')
