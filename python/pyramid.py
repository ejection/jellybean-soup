glBegin(GL_LINE_LOOP);


glVertex3f(0.5,-0.5,0.0);
glVertex3f(0.5,0.5,0.0);
glVertex3f(-0.5,0.5,0.0);
glVertex3f(-0.5,-0.5,0.0);
glEnd();
//draw the nose
glBegin(GL_LINES);

glVertex3f(0.5,-0.5,0.0);
//glColor3f(1.0,0.0,0.0);
glVertex3f(0.0,0.0,1);

//glColor3f(1.0,1.0,1.0);
glVertex3f(0.5,0.5,0.0);
//glColor3f(1.0,0.0,0.0);
glVertex3f(0.0,0.0,1);

//glColor3f(1.0,1.0,1.0);
glVertex3f(-0.5,0.5,0.0);
//glColor3f(1.0,0.0,0.0);
glVertex3f(0.0,0.0,1);

//glColor3f(1.0,1.0,1.0);
glVertex3f(-0.5,-0.5,0.0);
//	glColor3f(1.0,0.0,0.0);
glVertex3f(0.0,0.0,1);
glEnd();
