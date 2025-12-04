from .db_models import TemplateModel
from .nlp_utils import extract_placeholders, replace_placeholders

class TemplateEngine:
    """
    Engine for managing templates and generating letters.
    """

    def __init__(self):
        # Pre-loaded templates
        self.templates = {
            "student_leave": TemplateModel(
    name="student_leave",
    title=" Leave Letter",
    content=(
        "To\n{{greeting}},\nDepartment of {{department}},\n"
        "{{college name}}\n\n"
        "Respected Sir/Madam,\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll number}}, am a {{year}} Year student of {{department}} ({{section}}). "
        "I am writing to formally request leave from {{start date}} to {{end date}} due to {{reason}}.\n\n"
        "I have ensured that any urgent assignments or pending work have been noted, "
        "and I will make every effort to catch up on missed lectures and submissions upon my return. "
        "I would be grateful for your understanding and approval.\n\n"
        "Thank you for your consideration.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
    )
)
,"medical_leave": TemplateModel(
    name="medical_leave",
    title="Medical Leave Letter",
    content=(
        "To\n{{greeting}},\nDepartment of {{department}},\n"
        "{{college_name}}\n\n"
        "Respected Sir/Madam,\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "am writing to request medical leave from {{start_date}} to {{end_date}} due to {{medical_condition}}. "
        "I have consulted a doctor, and a medical certificate is attached for your reference.\n\n"
        "I will ensure that all missed lectures, assignments, and lab work are completed upon my return. "
        "I kindly request your approval for this leave and appreciate your understanding.\n\n"
        "Thank you for your consideration.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
        "Attachment: Medical Certificate\n"
    )
)
,"internship_permission": TemplateModel(
    name="internship_permission",
    title="Internship / Industrial Visit Permission Letter",
    content=(
        "To\n{{greeting}},\nDepartment of {{department}},\n"
        "{{college_name}}\n\n"
        "Respected Sir/Madam,\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "am writing to request permission to attend an internship/industrial visit at {{company_name}} from {{start_date}} to {{end_date}}. "
        "This internship/visit is relevant to my academic program and will provide practical exposure in {{field_or_domain}}.\n\n"
        "I assure you that I will complete all required documentation and will submit a report of my learning experience after completion. "
        "I kindly request your approval to proceed with this opportunity.\n\n"
        "Thank you for your consideration.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
    )
),"internship_application": TemplateModel(
    name="internship_application",
    title="Application for Internship to Company",
    content=(
        "To\n{{greeting}},\n{{company_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "Dear {{recipient_name}},\n\n"
        "I am {{name}}, a {{year}} Year student of {{department}} ({{section}}) at {{college_name}}, Roll No: {{roll_number}}. "
        "I am writing to express my interest in an internship position at {{company_name}} in the field of {{field_or_domain}} for the period {{start_date}} to {{end_date}}.\n\n"
        "During my academic program, I have gained knowledge in {{skills_or_courses}} and worked on projects such as {{project_name}}. "
        "I believe this internship will provide valuable practical experience and allow me to contribute to your team effectively.\n\n"
        "I have attached my resume and academic transcript for your review. I would be grateful for the opportunity to discuss my application further.\n\n"
        "Thank you for your time and consideration.\n\n"
        "Sincerely,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
        "Email: {{email}}\n"
        "Attachments: Resume, Transcript\n"
    )
),"project_extension_request": TemplateModel(
    name="project_extension_request",
    title="Project Deadline Extension Request Letter",
    content=(
        "To\n{{greeting}},\nDepartment of {{department}},\n"
        "{{college_name}}\n\n"
        "Respected Sir/Madam,\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "am writing on behalf of my project team (Members: {{team_members}}) to request an extension for submitting our project titled '{{project_title}}'.\n\n"
        "Due to {{reason_for_delay}}, we are unable to complete the project by the original deadline of {{original_deadline}}. "
        "We have completed {{completed_tasks}} and require additional time to finish {{pending_tasks}}.\n\n"
        "We kindly request an extension until {{proposed_new_deadline}} to submit the project. "
        "We assure you that we will utilize this time effectively and submit a high-quality project.\n\n"
        "Thank you for your understanding and consideration.\n\n"
        "Yours faithfully,\n"
        "{{team_leader_name}} on behalf of the team\n"
        "Team Members: {{team_members}}\n"
        "Roll Nos: {{team_roll_numbers}}\n"
        "Contact: {{contact_number}}\n"
    )
)
,"recommendation_request": TemplateModel(
    name="recommendation_request",
    title="Request for Recommendation / Reference Letter",
    content=(
        "To\n{{greeting}},\nDepartment of {{department}},\n"
        "{{college_name}}\n\n"
        "Respected {{recipient_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "am writing to kindly request your recommendation for {{purpose}} at {{organization_name}}.\n\n"
        "I had the privilege of attending your course {{course_name}} during {{semester}}, and I also worked on {{project_or_assignment}} under your guidance. "
        "Your recommendation highlighting my academic performance, skills, and work ethic would greatly support my application.\n\n"
        "The deadline for submission is {{deadline_date}}. I have attached my resume and transcript for your reference.\n\n"
        "Thank you very much for your time and consideration. I truly appreciate your support.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
        "Email: {{email}}\n"
        "Attachments: Resume, Transcript\n"
    )
)
,"revaluation_request": TemplateModel(
    name="revaluation_request",
    title="Re-evaluation / Exam Paper Rechecking Request Letter",
    content=(
        "To\n{{greeting}},\nController of Examinations,\n"
        "{{college_name}}\n\n"
        "Respected {{recipient_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "appeared for the {{exam_name}} held on {{exam_date}}. I request re-evaluation/rechecking of my answer paper for the course {{course_code}} - {{course_name}}.\n\n"
        "My obtained marks were {{obtained_marks}}, and I believe that a re-evaluation is necessary due to {{reason_for_request}}. "
        "I have enclosed the required application fee receipt (if applicable) for your reference.\n\n"
        "I kindly request you to consider my application and process the re-evaluation at the earliest.\n\n"
        "Thank you for your time and consideration.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
        "Attachment: Application Fee Receipt\n"
    )
)
,"certificate_request": TemplateModel(
    name="certificate_request",
    title="Bonafide / Enrollment / Character Certificate Request Letter",
    content=(
        "To\n{{greeting}},\nOffice of the Registrar,\n"
        "{{college_name}}\n\n"
        "Respected {{recipient_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "am writing to request issuance of a {{certificate_type}} for the purpose of {{purpose}}.\n\n"
        "My details are as follows:\n"
        "• Name: {{name}}\n"
        "• Roll No: {{roll_number}}\n"
        "• Program: {{program}}\n"
        "• Year: {{year}}\n\n"
        "I kindly request you to issue the certificate at your earliest convenience.\n\n"
        "Thank you for your support and consideration.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
    )
)
,"transfer_certificate_request": TemplateModel(
    name="transfer_certificate_request",
    title="Transfer / Migration Certificate Request Letter",
    content=(
        "To\n{{greeting}},\nOffice of the Registrar,\n"
        "{{college_name}}\n\n"
        "Respected {{recipient_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "am writing to request issuance of my {{certificate_type}} for the purpose of {{purpose}}.\n\n"
        "I have successfully completed my academic requirements at {{college_name}} and intend to continue my studies at {{new_institution}}. "
        "I kindly request you to process my certificate at the earliest to facilitate my admission process.\n\n"
        "My details are as follows:\n"
        "• Name: {{name}}\n"
        "• Roll No: {{roll_number}}\n"
        "• Program: {{program}}\n"
        "• Year: {{year}}\n\n"
        "Thank you for your assistance and prompt action.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
    )
)
,"training_completion_request": TemplateModel(
    name="training_completion_request",
    title="Internship / Training Completion Certificate Request Letter",
    content=(
        "To\n{{greeting}},\n{{organization_name}},\n\n"
        "Respected {{recipient_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}) at {{college_name}}, "
        "have successfully completed my internship/training at {{organization_name}} from {{start_date}} to {{end_date}} under the guidance of {{mentor_name}}.\n\n"
        "I kindly request you to issue a formal Internship/Training Completion Certificate stating the duration and nature of the training for my records and academic submission.\n\n"
        "Thank you for your support and guidance throughout the internship/training period.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
        "Email: {{email}}\n"
    )
)
,"hostel_request": TemplateModel(
    name="hostel_request",
    title="Hostel / Accommodation Request Letter",
    content=(
        "To\n{{greeting}},\nWarden, {{hostel_name}},\n"
        "{{college_name}}\n\n"
        "Respected {{recipient_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "am writing to request accommodation in {{hostel_name}} for the academic session {{session_year}}.\n\n"
        "Due to {{reason_for_request}}, I require a hostel room for the duration of {{duration}}. "
        "I assure you that I will abide by all hostel rules and maintain discipline during my stay.\n\n"
        "I kindly request you to consider my application and allot me a room at the earliest.\n\n"
        "Thank you for your support and consideration.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
        "Email: {{email}}\n"
    )
),"fee_concession_request": TemplateModel(
    name="fee_concession_request",
    title="Fee Concession / Scholarship Request Letter",
    content=(
        "To\n{{greeting}},\nThe Principal,\n"
        "{{college_name}}\n\n"
        "Respected {{recipient_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "am writing to request a fee concession/scholarship for the academic session {{session_year}} due to {{reason_for_request}}.\n\n"
        "I have consistently maintained {{academic_performance}} and actively participated in {{extracurricular_activities}}. "
        "I believe that a fee concession will greatly assist me in continuing my education without financial constraints.\n\n"
        "I have attached the necessary documents for your review and kindly request your consideration for approval.\n\n"
        "Thank you for your time and support.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
        "Email: {{email}}\n"
        "Attachments: Supporting Documents\n"
    )
),"complaint_letter": TemplateModel(
    name="complaint_letter",
    title="Complaint / Grievance Letter",
    content=(
        "To\n{{greeting}},\n{{department_or_office}},\n"
        "{{college_name}}\n\n"
        "Respected {{recipient_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "am writing to formally bring to your attention an issue regarding {{issue_description}}.\n\n"
        "Despite prior attempts to resolve the matter through {{previous_actions_taken}}, the problem persists. "
        "This issue is affecting my academic performance and overall experience at the college.\n\n"
        "I kindly request your immediate attention and intervention to address this matter at the earliest.\n\n"
        "Thank you for your understanding and support.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
        "Email: {{email}}\n"
    )
)
,"event_permission_request": TemplateModel(
    name="event_permission_request",
    title="Permission Letter for College Event / Extracurricular Activity",
    content=(
        "To\n{{greeting}},\n{{department_or_office}},\n"
        "{{college_name}}\n\n"
        "Respected {{recipient_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "on behalf of {{club_or_team_name}}, am writing to request permission to conduct/participate in {{event_name}} scheduled on {{event_date}} at {{event_location}}.\n\n"
        "The event aims to {{event_purpose}} and will involve {{number_of_participants}} participants. "
        "We will ensure that all college rules and safety guidelines are strictly followed.\n\n"
        "I kindly request your approval for this event and look forward to your support.\n\n"
        "Thank you for your time and consideration.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
        "Email: {{email}}\n"
    )
) ,"course_registration_request": TemplateModel(
    name="course_registration_request",
    title="Course Registration / Add-Drop Request Letter",
    content=(
        "To\n{{greeting}},\nDepartment of {{department}},\n"
        "{{college_name}}\n\n"
        "Respected {{recipient_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "am writing to request permission to {{action}} the course '{{course_name}}' for the {{semester}} semester. "
        "The reason for this request is {{reason_for_request}}.\n\n"
        "I kindly request your approval to proceed with this registration/add-drop process.\n\n"
        "Thank you for your consideration.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
        "Email: {{email}}\n"
    )
)
,"attendance_permission_request": TemplateModel(
    name="attendance_permission_request",
    title="Permission to Attend Exam Despite Low Attendance",
    content=(
        "To\n{{greeting}},\nDepartment of {{department}},\n"
        "{{college_name}}\n\n"
        "Respected {{recipient_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "am writing to request permission to appear for the {{exam_name}} scheduled on {{exam_date}}, "
        "despite having {{attendance_percentage}}% attendance in the course '{{course_name}}'.\n\n"
        "The reason for my low attendance is {{reason_for_low_attendance}}, and I assure you that I have been diligent in understanding the course material and completing assignments.\n\n"
        "I kindly request your approval to allow me to sit for the exam.\n\n"
        "Thank you for your understanding.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
        "Email: {{email}}\n"
    )
)
,"college_tour_leave_request": TemplateModel(
    name="college_tour_leave_request",
    title="Leave Request for College Tour / Study Trip",
    content=(
        "To\n{{greeting}},\nDepartment of {{department}},\n"
        "{{college_name}}\n\n"
        "Respected {{recipient_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "am writing to request leave from {{start_date}} to {{end_date}} to participate in the college-organized tour/study trip to {{tour_location}}.\n\n"
        "This trip is part of our academic/cultural activities, and I assure you that I will catch up on any missed classes or assignments.\n\n"
        "I kindly request your approval for this leave.\n\n"
        "Thank you for your consideration.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
        "Email: {{email}}\n"
    )
)
,"makeup_exam_request": TemplateModel(
    name="makeup_exam_request",
    title="Request for Make-up / Supplementary Exam",
    content=(
        "To\n{{greeting}},\nController of Examinations,\n"
        "{{college_name}}\n\n"
        "Respected {{recipient_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "was unable to appear for the {{exam_name}} held on {{exam_date}} due to {{reason_for_missing_exam}}.\n\n"
        "I kindly request permission to appear for a make-up/supplementary examination at a convenient date. "
        "I assure you that I will adhere to all examination rules and complete the assessment diligently.\n\n"
        "Thank you for your consideration.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
        "Email: {{email}}\n"
    )
)
,"transcript_request": TemplateModel(
    name="transcript_request",
    title="Grade / Transcript Request Letter",
    content=(
        "To\n{{greeting}},\nOffice of the Registrar,\n"
        "{{college_name}}\n\n"
        "Respected {{recipient_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "am writing to request the issuance of my official grade/transcript for {{purpose}}.\n\n"
        "I have completed all required coursework and formalities, and I kindly request you to process my transcript at the earliest to facilitate {{reason_for_request}}.\n\n"
        "Thank you for your assistance.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
        "Email: {{email}}\n"
    )
)
,"academic_counseling_request": TemplateModel(
    name="academic_counseling_request",
    title="Request for Academic Counseling / Mentorship Meeting",
    content=(
        "To\n{{greeting}},\nDepartment of {{department}},\n"
        "{{college_name}}\n\n"
        "Respected {{recipient_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "am writing to request an appointment for academic counseling/mentorship to discuss {{topic_or_issue}}.\n\n"
        "I seek your guidance regarding {{specific_concerns}} and believe that your advice will greatly assist me in improving my academic performance and planning my future courses/projects.\n\n"
        "I kindly request a convenient date and time for the meeting.\n\n"
        "Thank you for your support and guidance.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
        "Email: {{email}}\n"
    )
)
,"hostel_room_change_request": TemplateModel(
    name="hostel_room_change_request",
    title="Hostel / Room Change Request Letter",
    content=(
        "To\n{{greeting}},\nWarden, {{hostel_name}},\n"
        "{{college_name}}\n\n"
        "Respected {{recipient_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "am writing to request a change of my hostel room from {{current_room_number}} to {{requested_room_number}} due to {{reason_for_request}}.\n\n"
        "I assure you that I will comply with all hostel rules and maintain discipline. I kindly request your approval for this room change at the earliest.\n\n"
        "Thank you for your consideration.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
        "Email: {{email}}\n"
    )
)
,"library_access_request": TemplateModel(
    name="library_access_request",
    title="Library Membership / Access Request Letter",
    content=(
        "To\n{{greeting}},\nLibrarian, {{library_name}},\n"
        "{{college_name}}\n\n"
        "Respected {{recipient_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "am writing to request library membership/access to {{library_name}} to utilize resources for my academic activities, research, and assignments.\n\n"
        "I kindly request you to grant me the necessary access and provide any required guidelines for library usage.\n\n"
        "Thank you for your support.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
        "Email: {{email}}\n"
    )
)
,"facilities_complaint_letter": TemplateModel(
    name="facilities_complaint_letter",
    title="Complaint Letter Regarding College Facilities",
    content=(
        "To\n{{greeting}},\n{{department_or_office}},\n"
        "{{college_name}}\n\n"
        "Respected {{recipient_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "am writing to formally bring to your attention an issue regarding {{facility_issue_description}}.\n\n"
        "Despite previous attempts to resolve this matter through {{previous_actions_taken}}, the problem persists. "
        "This issue is affecting the academic and personal experience of the students.\n\n"
        "I kindly request your immediate attention and intervention to address this matter.\n\n"
        "Thank you for your understanding and support.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
        "Email: {{email}}\n"
    )
)
,"duplicate_id_request": TemplateModel(
    name="duplicate_id_request",
    title="Request for Student ID / Duplicate ID Card",
    content=(
        "To\n{{greeting}},\nOffice of the Registrar,\n"
        "{{college_name}}\n\n"
        "Respected {{recipient_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "am writing to request the issuance of a duplicate student ID card as my previous ID was {{reason_for_duplicate_request}}.\n\n"
        "I kindly request you to process this request at the earliest so that I may continue to access college facilities without interruption.\n\n"
        "Thank you for your assistance.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
        "Email: {{email}}\n"
    )
)
,"bus_pass_request": TemplateModel(
    name="bus_pass_request",
    title="College Transportation / Bus Pass Request Letter",
    content=(
        "To\n{{greeting}},\nTransport Office,\n"
        "{{college_name}}\n\n"
        "Respected {{recipient_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "am writing to request the issuance/renewal of my college bus pass for the academic session {{session_year}}.\n\n"
        "I will be using the bus facility to commute from {{residential_address}} to the college daily. "
        "I kindly request you to process my application at the earliest and inform me of any documents or fees required.\n\n"
        "Thank you for your support.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
        "Email: {{email}}\n"
    )
)
,"internship_extension_resignation": TemplateModel(
    name="internship_extension_resignation",
    title="Internship Extension / Resignation Letter",
    content=(
        "To\n{{greeting}},\n{{organization_name}},\n\n"
        "Respected {{recipient_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, a student of {{college_name}}, Roll No: {{roll_number}}, am writing regarding my internship at {{organization_name}}.\n\n"
        "I would like to {{action}} my internship, originally scheduled from {{start_date}} to {{end_date}}, due to {{reason_for_request}}.\n\n"
        "I kindly request your consideration and guidance regarding this matter. I am grateful for the learning opportunities provided during my internship.\n\n"
        "Thank you for your time and support.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
        "Email: {{email}}\n"
    )
),"job_recommendation_request": TemplateModel(
    name="job_recommendation_request",
    title="Placement / Job Recommendation Request Letter",
    content=(
        "To\n{{greeting}},\n{{department_or_office}},\n"
        "{{college_name}}\n\n"
        "Respected {{recipient_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "am writing to request your recommendation/reference for placement/job opportunities at {{company_name}}.\n\n"
        "I have completed {{relevant_courses_or_projects}} and believe that your recommendation will significantly support my application. "
        "I kindly request your assistance and guidance in this regard.\n\n"
        "Thank you for your time and support.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
        "Email: {{email}}\n"
    )
)
,"project_mentor_request": TemplateModel(
    name="project_mentor_request",
    title="Project Mentor Request / Supervisor Change Letter",
    content=(
        "To\n{{greeting}},\nHead of {{department}},\n"
        "{{college_name}}\n\n"
        "Respected {{recipient_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "am writing to request {{request_type}} for my project titled '{{project_title}}'.\n\n"
        "The reason for this request is {{reason_for_request}}. "
        "I believe that {{justification}} will help me achieve better guidance and successful completion of my project.\n\n"
        "I kindly request your consideration and approval for this request.\n\n"
        "Thank you for your support.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
        "Email: {{email}}\n"
    )
)
,"competition_permission_request": TemplateModel(
    name="competition_permission_request",
    title="Hackathon / Competition Participation Permission Letter",
    content=(
        "To\n{{greeting}},\n{{department_or_office}},\n"
        "{{college_name}}\n\n"
        "Respected {{recipient_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "am writing to request permission to participate in the {{competition_name}} scheduled on {{competition_date}} at {{competition_location}}.\n\n"
        "This competition aims to {{competition_purpose}} and will involve {{number_of_participants}} participants from our college. "
        "We will ensure full adherence to college rules and guidelines.\n\n"
        "I kindly request your approval for my participation.\n\n"
        "Thank you for your support.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
        "Email: {{email}}\n"
    )
),"medical_certificate_submission": TemplateModel(
    name="medical_certificate_submission",
    title="Medical Certificate Submission Letter",
    content=(
        "To\n{{greeting}},\nOffice of the Registrar / Department of {{department}},\n"
        "{{college_name}}\n\n"
        "Respected {{recipient_name}},\n\n"
        "Subject: {{subject}}\n\n"
        "I, {{name}}, Roll No: {{roll_number}}, a {{year}} Year student of {{department}} ({{section}}), "
        "am submitting my medical certificate for the period from {{start_date}} to {{end_date}} due to {{reason_for_medical_leave}}.\n\n"
        "I kindly request you to record my absence accordingly and grant necessary consideration for any missed academic work or examinations.\n\n"
        "Thank you for your understanding.\n\n"
        "Yours faithfully,\n"
        "{{name}}\n"
        "Roll No: {{roll_number}}\n"
        "Contact: {{contact_number}}\n"
        "Email: {{email}}\n"
        "Attachment: Medical Certificate\n"
    )
)

}

    def get_template(self, template_key: str):
        return self.templates.get(template_key, None)

    def get_placeholders(self, template_key: str):
        template = self.get_template(template_key)
        if not template:
            return []
        return extract_placeholders(template.content)

    def generate_letter(self, template_key: str, data: dict):
        template = self.get_template(template_key)
        if not template:
            return "❌ Template not found"
        # Ensure 'subject' exists in data to avoid missing placeholder
        if 'subject' not in data:
            data['subject'] = ""
        return replace_placeholders(template.content, data)

    def list_templates(self):
        return [{"key": k, "title": v.title} for k, v in self.templates.items()]


# Singleton instance
engine_instance = TemplateEngine()
def render_letter(template_key, data):
    return engine_instance.generate_letter(template_key, data)
