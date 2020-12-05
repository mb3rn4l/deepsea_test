from django.core.mail import EmailMultiAlternatives
from celery.decorators import task, periodic_task


@task()
def send_creation_team_email(team_name):
    """
    Send a email when a team is created
    :param team_name: name of the team created
    """
    subject, from_email, to = 'creacion de equipos', 'miguel.bernal.colonia@gmail.com', 'donberna-93@hotmail.com'
    text_content = 'Se creo el equipo nuevo {}.'.format(team_name)
    html_content = '<p>Se creo el equipo nuevo <strong>{}</strong>.</p>'.format(team_name)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
