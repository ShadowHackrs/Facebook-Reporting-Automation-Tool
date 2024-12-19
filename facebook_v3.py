from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from termcolor import colored
import time
import sys
import random
import base64

# === Enhancing Visuals ===
def animate_text(text, color="green", delay=0.01):
    """Print animated text with color and delay."""
    for char in text:
        sys.stdout.write(colored(char, color))
        sys.stdout.flush()
        time.sleep(delay)
    print()

def enhanced_banner():
    """Display an animated banner with Syrian revolution flag."""
    banner = """
    \033[32m▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒
    \033[32m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    \033[32m▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\033[0m
    \033[37m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
           \033[31m★                 ★                 ★\033[0m
    \033[37m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\033[0m
    \033[30m▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    \033[30m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    \033[30m▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\033[0m

         \033[1mFB Auto Report - Syrian Revolution Edition\033[0m
              Designed with pride - By Shadow Hacker     

         \033[36mFacebook:   https://www.fb.com/Tareq.DJX\033[0m
         \033[34mTwitter:    https://www.x.com/ShadowHackrs\033[0m
         \033[35mInstagram:  https://instagram.com/shadowhackr\033[0m
         \033[32mWebsite:   https://www.arbgit.com\033[0m                                                                                     
    """
    border = "═" * 60
    animate_text(border, "cyan")
    print(banner)  # Print the banner directly to preserve ANSI colors
    animate_text(border, "cyan")
    animate_text("=== Welcome to the Advanced Reporting Tool ===", "yellow", delay=0.03)

# === Matrix-style Animation ===
def hacker_symbol_rain(rows=15, width=50, delay=0.05):
    """Create a cascading 'Matrix-style' symbol rain effect."""
    symbols = ["0", "1", "▓", "░", "≡", "S", "H", "A", "D", "O", "H", "A", "C", "R"]
    colors = ["green", "yellow", "cyan"]

    for _ in range(rows):
        line = " " * random.randint(0, width // 3) + "".join(random.choice(symbols) for _ in range(width))
        color = random.choice(colors)
        sys.stdout.write(colored(line, color) + "\n")
        sys.stdout.flush()
        time.sleep(delay)

# === Email Obfuscation ===
def obfuscate_email(email):
    """Return a base64-obfuscated email string."""
    encoded = base64.b64encode(email.encode()).decode()
    return f"*** {encoded[:4]}...{encoded[-4:]} ***"

# === Multi-Report Feature ===
def get_report_count():
    """Ask the user how many times to report."""
    while True:
        try:
            count = int(input(colored("Enter the number of times to report: ", "blue")))
            if count > 0:
                animate_text(f"You selected to report {count} times.", "green")
                return count
            else:
                print(colored("Please enter a positive number.", "red"))
        except ValueError:
            print(colored("Invalid input. Please enter a valid number.", "red"))

# === Helper Functions ===
def create_driver(user_agent=None):
    """Create and configure a WebDriver instance with proxy and anti-detection measures."""
    chrome_options = Options()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    
    # Anti-detection measures
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # Random user-agent if none provided
    if not user_agent:
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"
        ]
        user_agent = random.choice(user_agents)
    
    chrome_options.add_argument(f"user-agent={user_agent}")
    
    # Additional anti-detection
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-infobars")
    
    # Proxy support
    proxies = setup_proxy_rotation()
    if proxies:
        proxy = get_random_proxy(proxies)
        if proxy:
            chrome_options.add_argument(f'--proxy-server={proxy}')
    
    return webdriver.Chrome(options=chrome_options)

def login(driver, email, password):
    """Log in to the Facebook account."""
    obfuscated_email = obfuscate_email(email)
    animate_text(f"Logging in with account: {obfuscated_email}", "cyan")
    driver.get("https://www.facebook.com/")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "email"))).send_keys(email)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "pass"))).send_keys(password)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "login"))).click()
    time.sleep(5)
    if "login" in driver.current_url:
        raise Exception(f"Failed to login with {obfuscated_email}. Check credentials.")

def detect_and_report(driver, account_url, report_type, sub_option, report_count):
    """Perform the reporting actions with enhanced button detection."""
    for _ in range(report_count):
        driver.get(account_url)
        time.sleep(3)
        animate_text("Analyzing page elements...", "cyan")

        # Enhanced menu detection for different page types
        try:
            # Try multiple menu button patterns
            menu_patterns = [
                (By.CSS_SELECTOR, 'div[aria-label="See options"]'),
                (By.CSS_SELECTOR, 'div[aria-label="Actions"]'),
                (By.CSS_SELECTOR, 'div[aria-label="More"]'),
                (By.CSS_SELECTOR, 'div[aria-label="Additional actions"]'),
                (By.CSS_SELECTOR, 'div[aria-label="Group menu"]'),
                (By.CSS_SELECTOR, 'div[aria-label="Page menu"]'),
                (By.XPATH, "//div[contains(@aria-label, 'menu')]"),
                (By.XPATH, "//div[contains(@aria-label, 'More')]"),
                (By.XPATH, "//div[contains(@aria-label, 'options')]"),
                # Arabic menu patterns
                (By.CSS_SELECTOR, 'div[aria-label="خيارات"]'),
                (By.CSS_SELECTOR, 'div[aria-label="المزيد"]'),
                (By.CSS_SELECTOR, 'div[aria-label="قائمة"]'),
                (By.XPATH, "//div[contains(@aria-label, 'خيارات')]"),
                (By.XPATH, "//div[contains(@aria-label, 'قائمة')]")
            ]

            menu_found = False
            for by_type, pattern in menu_patterns:
                try:
                    menu_button = WebDriverWait(driver, 3).until(
                        EC.element_to_be_clickable((by_type, pattern))
                    )
                    menu_button.click()
                    menu_found = True
                    animate_text("Menu accessed successfully", "green")
                    break
                except:
                    continue

            if not menu_found:
                # Try finding by class names commonly used for menu buttons
                class_patterns = [
                    "sp_dOWqGfXHGYs",
                    "_4xev",
                    "_3qn7",
                    "_2yq",
                    "_6_",
                    "_3-8_",
                    "_4-lx"
                ]
                
                for class_name in class_patterns:
                    try:
                        menu_button = WebDriverWait(driver, 2).until(
                            EC.element_to_be_clickable((By.CLASS_NAME, class_name))
                        )
                        menu_button.click()
                        menu_found = True
                        animate_text("Menu accessed via class pattern", "green")
                        break
                    except:
                        continue

            if not menu_found:
                raise Exception("Menu button not found")

        except Exception as e:
            animate_text(f"Menu detection failed: {str(e)}", "red")
            return

        # Enhanced report option detection
        try:
            report_patterns = [
                f"//span[contains(text(), '{report_type}')]",
                f"//a[contains(text(), '{report_type}')]",
                f"//div[contains(text(), '{report_type}')]",
                "//span[contains(text(), 'Report')]",
                "//a[contains(text(), 'Report')]",
                # Arabic patterns
                "//span[contains(text(), 'إبلاغ')]",
                "//span[contains(text(), 'تبليغ')]",
                "//a[contains(text(), 'إبلاغ')]",
                "//a[contains(text(), 'تبليغ')]"
            ]

            report_found = False
            for pattern in report_patterns:
                try:
                    report_button = WebDriverWait(driver, 3).until(
                        EC.element_to_be_clickable((By.XPATH, pattern))
                    )
                    report_button.click()
                    report_found = True
                    animate_text("Report option selected", "green")
                    break
                except:
                    continue

            if not report_found:
                raise Exception("Report option not found")

        except Exception as e:
            animate_text(f"Report option detection failed: {str(e)}", "red")
            return

        # Select report type with enhanced detection
        try:
            type_patterns = [
                f"//span[contains(text(), '{report_type}')]",
                f"//a[contains(text(), '{report_type}')]",
                f"//div[contains(text(), '{report_type}')]",
                # Add Arabic translations if needed
                f"//span[contains(text(), '{translate_to_arabic(report_type)}')]",
                f"//a[contains(text(), '{translate_to_arabic(report_type)}')]"
            ]

            type_found = False
            for pattern in type_patterns:
                try:
                    type_button = WebDriverWait(driver, 3).until(
                        EC.element_to_be_clickable((By.XPATH, pattern))
                    )
                    type_button.click()
                    type_found = True
                    animate_text(f"Selected report type: {report_type}", "green")
                    break
                except:
                    continue

            if not type_found:
                raise Exception("Report type option not found")

        except Exception as e:
            animate_text(f"Report type selection failed: {str(e)}", "red")
            return

        # Handle sub-option if available
        if sub_option:
            try:
                sub_option_patterns = [
                    f"//span[contains(text(), '{sub_option}')]",
                    f"//a[contains(text(), '{sub_option}')]",
                    f"//div[contains(text(), '{sub_option}')]",
                    # Add Arabic translations if needed
                    f"//span[contains(text(), '{translate_to_arabic(sub_option)}')]",
                    f"//a[contains(text(), '{translate_to_arabic(sub_option)}')]"
                ]

                sub_option_found = False
                for pattern in sub_option_patterns:
                    try:
                        sub_option_button = WebDriverWait(driver, 3).until(
                            EC.element_to_be_clickable((By.XPATH, pattern))
                        )
                        sub_option_button.click()
                        sub_option_found = True
                        animate_text(f"Selected sub-option: {sub_option}", "green")
                        break
                    except:
                        continue

                if not sub_option_found:
                    animate_text(f"Sub-option selection skipped", "yellow")

            except Exception as e:
                animate_text(f"Sub-option selection failed: {str(e)}", "yellow")

        # Smart button handling for final submission
        handle_submit_or_done(driver)

def translate_to_arabic(text):
    """Basic translation mapping for common terms"""
    translations = {
        "Report": "إبلاغ",
        "Submit": "إرسال",
        "Done": "تم",
        "Next": "التالي",
        "Cancel": "إلغاء",
        "Spam": "بريد مزعج",
        "Fake": "مزيف",
        "Harassment": "تحرش",
        "Violence": "عنف",
        "Hate": "كراهية",
        "False information": "معلومات خاطئة",
        "Something else": "شيء آخر"
    }
    return translations.get(text, text)  # Return original if no translation found

def handle_submit_or_done(driver):
    """Enhanced submit/done button handler with multiple detection patterns"""
    button_patterns = {
        'submit': [
            "//span[text()='Submit']",
            "//span[text()='إرسال']",
            "//button[contains(text(), 'Submit')]",
            "//button[contains(text(), 'إرسال')]",
            "//div[contains(@aria-label, 'Submit')]",
            "//div[contains(@aria-label, 'إرسال')]"
        ],
        'done': [
            "//span[text()='Done']",
            "//span[text()='تم']",
            "//button[contains(text(), 'Done')]",
            "//button[contains(text(), 'تم')]",
            "//div[contains(@aria-label, 'Done')]",
            "//div[contains(@aria-label, 'تم')]"
        ],
        'next': [
            "//span[text()='Next']",
            "//span[text()='التالي']",
            "//button[contains(text(), 'Next')]",
            "//button[contains(text(), 'التالي')]"
        ]
    }

    # Try submit patterns first
    for pattern in button_patterns['submit']:
        try:
            button = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, pattern))
            )
            button.click()
            animate_text("Report submitted successfully", "green")
            return True
        except:
            continue

    # Try done patterns
    for pattern in button_patterns['done']:
        try:
            button = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, pattern))
            )
            button.click()
            animate_text("Report completed successfully", "green")
            return True
        except:
            continue

    # Try next patterns as last resort
    for pattern in button_patterns['next']:
        try:
            button = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, pattern))
            )
            button.click()
            animate_text("Proceeding to next step", "yellow")
            time.sleep(2)  # Wait for next screen
            # Recursively try submit/done again
            return handle_submit_or_done(driver)
        except:
            continue

    animate_text("Could not find submit/done button", "red")
    return False

# === Report Types ===
report_structure = {
    "Report profile": {
        "Something about this profile": [
            "Pretending to be someone",
            "Fake account",
            "Fake name",
            "Harassment or bullying",
            "Something else",
            "I want to help"
        ],
        "A specific post": ["Spam"],
        "Pretending to be someone": [
            "Me", "A friend", "Celebrity", "A business"
        ],
        "Fake account": [],
        "Fake name": [],
        "Posting inappropriate things": [],
        "Harassment or bullying": [],
        "I want to help": [],
        "Something else": []
    },
    "Report group": {
        "Nudity or sexual activity": [],
        "Bullying or harassment": [],
        "Suicide, self-injury or eating disorders": [],
        "Violence, hate or exploitation": [],
        "Selling or promoting restricted items": [],
        "Fraud or scam": [],
        "Spam": [],
        "False information": [],
        "Intellectual property": []
    },
    "Report page": {
        "Problem involving someone under 18": [],
        "Bullying, harassment or abuse": [],
        "Suicide or self-harm": [],
        "Violent, hateful or disturbing content": [],
        "Selling or promoting restricted items": [],
        "Adult content": [],
        "Scam, fraud or false information": [],
        "Fake profile": [],
        "Something else": []
    }
}

# === New Feature: Proxy Support and Anti-Ban Mechanisms ===
def setup_proxy_rotation():
    """Setup and manage proxy rotation for anti-ban."""
    proxies = []
    try:
        with open("proxies.txt", "r") as f:
            proxies = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        animate_text("No proxies.txt found. Running without proxy rotation.", "yellow")
    return proxies

def get_random_proxy(proxies):
    """Get a random proxy from the list."""
    return random.choice(proxies) if proxies else None

# === New Feature: Smart Delay System ===
class SmartDelay:
    def __init__(self):
        self.base_delay = 2
        self.success_count = 0
        self.failure_count = 0
        
    def calculate_delay(self):
        """Calculate dynamic delay based on success/failure ratio."""
        if self.failure_count > 3:
            return min(self.base_delay * 2, 10)  # Max 10 seconds
        if self.success_count > 5:
            return max(self.base_delay * 0.75, 1)  # Min 1 second
        return self.base_delay
    
    def report_success(self):
        self.success_count += 1
        self.failure_count = max(0, self.failure_count - 1)
        
    def report_failure(self):
        self.failure_count += 1
        self.success_count = max(0, self.success_count - 1)

# === New Feature: Session Management ===
class SessionManager:
    def __init__(self):
        self.session_id = base64.b64encode(str(time.time()).encode()).decode()[:8]
        self.start_time = time.time()
        self.report_history = []
        
    def log_report(self, url, success, error=None):
        """Log report attempt with details."""
        self.report_history.append({
            'timestamp': time.time(),
            'url': url,
            'success': success,
            'error': str(error) if error else None
        })
    
    def get_session_stats(self):
        """Get detailed session statistics."""
        total_reports = len(self.report_history)
        successful_reports = sum(1 for r in self.report_history if r['success'])
        return {
            'session_id': self.session_id,
            'duration': time.time() - self.start_time,
            'total_reports': total_reports,
            'success_rate': (successful_reports / total_reports * 100) if total_reports else 0
        }

# === New Feature: Error Recovery ===
def handle_facebook_errors(driver):
    """Handle common Facebook errors and restrictions."""
    try:
        # Check for temporary block
        if "You're Temporarily Blocked" in driver.page_source:
            animate_text("Temporary block detected. Switching proxy...", "yellow")
            return False
            
        # Check for security check
        if "security check" in driver.page_source.lower():
            animate_text("Security check detected. Implementing evasion...", "yellow")
            time.sleep(random.uniform(20, 30))  # Random delay
            return False
            
        # Check for rate limiting
        if "try again later" in driver.page_source.lower():
            animate_text("Rate limit detected. Adjusting delays...", "yellow")
            time.sleep(random.uniform(60, 120))  # Longer delay
            return False
            
        return True
    except Exception as e:
        animate_text(f"Error in error handling: {str(e)}", "red")
        return False

# === New Feature: Advanced Browser Fingerprint Randomization ===
def randomize_browser_fingerprint(driver):
    """Randomize browser fingerprint to avoid detection."""
    try:
        # Execute JavaScript to randomize canvas fingerprint
        driver.execute_script("""
            const originalToDataURL = HTMLCanvasElement.prototype.toDataURL;
            HTMLCanvasElement.prototype.toDataURL = function(type) {
                if (type === 'image/png' && this.width === 220 && this.height === 30) {
                    return originalToDataURL.apply(this, arguments);
                }
                const context = this.getContext('2d');
                const shift = Math.random() * 10;
                const data = context.getImageData(0, 0, this.width, this.height);
                for (let i = 0; i < data.data.length; i += 4) {
                    data.data[i] = data.data[i] + shift;
                }
                context.putImageData(data, 0, 0);
                return originalToDataURL.apply(this, arguments);
            };
        """)
        
        # Randomize WebGL fingerprint
        driver.execute_script("""
            const getParameter = WebGLRenderingContext.prototype.getParameter;
            WebGLRenderingContext.prototype.getParameter = function(parameter) {
                if (parameter === 37445) {
                    return 'Intel Open Source Technology Center';
                }
                if (parameter === 37446) {
                    return 'Mesa DRI Intel(R) HD Graphics (SKL GT2)';
                }
                return getParameter.apply(this, arguments);
            };
        """)
    except Exception as e:
        animate_text(f"Error in fingerprint randomization: {str(e)}", "yellow")

# === Choosing Report Type ===
def choose_report_type():
    """Allow the user to choose a report type."""
    animate_text("\nAvailable report categories:", "yellow")
    categories = list(report_structure.keys())
    for idx, category in enumerate(categories, start=1):
        print(colored(f"{idx}. {category}", "cyan"))
    while True:
        try:
            category_choice = int(input(colored("\nChoose the number of the report category: ", "blue")))
            if 1 <= category_choice <= len(categories):
                selected_category = categories[category_choice - 1]
                animate_text(f"Selected category: {selected_category}", "green")
                
                # List report types within the selected category
                animate_text("\nAvailable report types:", "yellow")
                report_types = list(report_structure[selected_category].keys())
                for idx, report_type in enumerate(report_types, start=1):
                    print(colored(f"{idx}. {report_type}", "cyan"))
                
                while True:
                    try:
                        type_choice = int(input(colored("\nChoose the number of the report type: ", "blue")))
                        if 1 <= type_choice <= len(report_types):
                            selected_type = report_types[type_choice - 1]
                            animate_text(f"Selected report type: {selected_type}", "green")
                            return selected_category, selected_type
                        else:
                            print(colored("Invalid choice. Please choose a valid number.", "red"))
                    except ValueError:
                        print(colored("Invalid input. Please enter a number.", "red"))
            else:
                print(colored("Invalid choice. Please choose a valid number.", "red"))
        except ValueError:
            print(colored("Invalid input. Please enter a number.", "red"))

def choose_sub_option(selected_category, selected_type):
    """Allow the user to choose a sub-option for the selected report type."""
    sub_options = report_structure[selected_category][selected_type]
    if sub_options:
        animate_text(f"\nAvailable sub-options for {selected_type}:", "yellow")
        for idx, option in enumerate(sub_options, start=1):
            print(colored(f"{idx}. {option}", "cyan"))
        while True:
            try:
                choice = int(input(colored("\nChoose the number of the sub-option: ", "blue")))
                if 1 <= choice <= len(sub_options):
                    selected_sub_option = sub_options[choice - 1]
                    animate_text(f"Selected sub-option: {selected_sub_option}", "green")
                    return selected_sub_option
                else:
                    print(colored("Invalid choice. Please choose a valid number.", "red"))
            except ValueError:
                print(colored("Invalid input. Please enter a number.", "red"))
    else:
        animate_text(f"No sub-options available for {selected_type}.", "yellow")
    return None

# === Load URLs and Accounts ===
def load_urls_and_accounts():
    """Load URLs and accounts from files."""
    try:
        with open("urls.txt", "r") as f:
            account_urls = [line.strip() for line in f if line.strip()]
        with open("accounts.txt", "r") as f:
            accounts = [line.strip().split(":") for line in f if line.strip()]
        return account_urls, accounts
    except FileNotFoundError as e:
        animate_text(f"Error loading files: {str(e)}", "red")
        sys.exit(1)

# === Execute Reports ===
def execute_reports():
    """Execute the reporting process with enhanced features."""
    try:
        enhanced_banner()
        print("\n" + colored("=" * 60, 'cyan'))
        
        # Initialize new features
        session_manager = SessionManager()
        smart_delay = SmartDelay()
        
        # Load configuration
        loading_animation("Loading configuration and accounts...")
        urls, accounts = load_urls_and_accounts()
        show_success(f"Loaded {len(urls)} URLs and {len(accounts)} accounts")
        
        # Get report settings
        show_info("Setting up report configuration...")
        report_count = get_report_count()
        selected_category, selected_type = choose_report_type()
        selected_sub_option = choose_sub_option(selected_category, selected_type)
        
        total_reports = len(urls) * len(accounts) * report_count
        current_report = 0
        
        for email, password in accounts:
            driver = create_driver()
            try:
                # Enhanced login security
                loading_animation("Securing connection and logging in...")
                randomize_browser_fingerprint(driver)
                login(driver, email, password)
                show_success("Login successful - Connection secured")
                
                for url in urls:
                    for _ in range(report_count):
                        current_report += 1
                        
                        # Show progress
                        print(fancy_progress_bar(current_report, total_reports))
                        loading_animation(f"Processing report for: {url[:40]}...")
                        
                        try:
                            # Check for Facebook errors
                            if not handle_facebook_errors(driver):
                                driver.quit()
                                driver = create_driver()  # Create new session
                                login(driver, email, password)
                            
                            # Report process with smart delay
                            detect_and_report(driver, url, selected_type, selected_sub_option, 1)
                            smart_delay.report_success()
                            session_manager.log_report(url, True)
                            show_success(f"Report {current_report} completed successfully")
                            
                        except Exception as e:
                            smart_delay.report_failure()
                            session_manager.log_report(url, False, e)
                            show_error(f"Report failed: {str(e)}")
                        
                        # Apply smart delay
                        time.sleep(smart_delay.calculate_delay())
                
            except Exception as e:
                show_error(f"Account error: {str(e)}")
            finally:
                driver.quit()
        
        # Show detailed session statistics
        stats = session_manager.get_session_stats()
        show_stats(stats)
        
        print("\n" + colored("🎉 Mission Accomplished! 🎉", 'green'))
        print(colored("=" * 60, 'cyan'))
        
    except Exception as e:
        show_error(f"Critical error: {str(e)}")

def loading_animation(text, duration=2):
    """Display a beautiful loading animation."""
    frames = ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        frame = colored(frames[i % len(frames)], 'cyan')
        print(f'\r{frame} {text}', end='')
        time.sleep(0.1)
        i += 1
    print()

def rainbow_text(text):
    """Display text in rainbow colors."""
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    colored_chars = [colored(char, colors[i % len(colors)]) for i, char in enumerate(text)]
    return ''.join(colored_chars)

def show_success(message):
    """Display a success message with sparkles."""
    print(colored(f"\r✨ {message} ✨", 'green'))
    time.sleep(0.5)

def show_error(message):
    """Display an error message with icon."""
    print(colored(f"\r⚠️  {message}", 'red'))
    time.sleep(0.5)

def show_info(message):
    """Display an info message with icon."""
    print(colored(f"\rℹ️  {message}", 'blue'))
    time.sleep(0.3)

def fancy_progress_bar(current, total, width=40):
    """Show a fancy progress bar with percentage and count."""
    progress = current / total
    filled = int(width * progress)
    bar = colored('█' * filled, 'cyan') + colored('░' * (width - filled), 'white')
    percentage = colored(f"{int(progress * 100)}%", 'yellow')
    count = colored(f"({current}/{total})", 'green')
    return f"\r|{bar}| {percentage} {count}"

def show_stats(stats):
    """Display beautiful statistics."""
    print("\n" + colored("📊 Statistics 📊", 'cyan'))
    for key, value in stats.items():
        print(colored(f"• {key}: ", 'yellow') + colored(str(value), 'white'))

# === Main Program ===
if __name__ == "__main__":
    execute_reports()
